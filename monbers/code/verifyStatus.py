import urllib.request
import csv
import qrcode
import webbrowser
import requests
import sys
import pandas as pd
from selenium import webdriver
# email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage
import smtplib

# Member verification and download the images from google drive
def verifyMember(p_link, status, payment):
    """
    :param p_link: the link of the student profile
    :return: true if the page is valid and contains student
    otherwise no
    """
    # without doctoral
    # more than 5 student or etudiant

    if status != 'Bachelor/Master student':
        if payment == 'Yes':
            return True
        return False

    try:
        # the driver needs to be installed to use the following block
        browser = webdriver.Firefox()
        browser.get(p_link)
        web_page = browser.page_source
        browser.quit()

        if '<a href="#">Student	</a>' in web_page:
            return True
        elif '<a href="#">Etudiant	</a>' in web_page:
            return True
        else:
            return False
    except:
        print ("http request failed. Member is not verified")
    return False

def generateQR(link):
    # Create qr code instance
    # QR code links to the generated link for each member
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data
    qr.add_data(link)
    qr.make(fit=True)

    qr_code = qr.make_image()
    temp_location = 'image.jpg'
    
    qr_code.save(temp_location)

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def generateMemberPage(firstN, lastN, status, validity, img_path):
    # init file constants
    status = status
    exp_date = '2019.01.01'

    file_name = '../../members/' + firstN + '_' + lastN + '.md'

    # writing to file
    file = open(file_name, "w+")
    file.write('---\nlayout: post\n')
    file.write('title: ' + firstN + ' ' + lastN + '\n---\n\nStatus: ' + status + '\n')
    file.write('\nExpiration date: ' + exp_date + '\n')
    if validity:
        file.write('\nValidity: ' + '<font color="green"> Verified</font> \n')
    else:
        file.write('\nValidity: ' + '<font color="red"> Not valid</font> \n')

    file.write('![](/members/' + img_path + ')\n')
    file.write('![](/members/img/bar.png)\n')

    file.close()

def send_email(dest_email):
    attachment = 'image.jpg'

    msg = MIMEMultipart()
    msg["To"] = "clubMontagne2018@gmail.com"
    msg["From"] = "clubMontagne2018@gmail.com"
    msg["Subject"] = "Your membership QR code"
    text = """\
        Salut!

        Here is your membership card for Club Montagne at EPFL 
        
        If you have any questions or suggestions, feel free to email
            
        clubMontagne2018@gmail.com. 

        Cheers,
        
        Club Montagne 
    """

    content = MIMEText(text, 'plain')
    msg.attach(content)

    fp = open(attachment, 'rb')
    msgText = MIMEImage(fp.read())
    msg.attach(msgText)  # Added, and edited the previous line

    print(msg.as_string())

    ## send email
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('clubMontagne2018@gmail.com', '7CD')

    mailserver.sendmail('clubMontagne2018@gmail.com', dest_email, msg.as_string())

    mailserver.quit()

def process_info(info_path, photo_path):
    df = pd.read_csv(info_path)
    validities = []
    wrong_emails = []
    for index, row in df.iterrows():
        # 1. validate member page
        validities.append(verifyMember(row['EPFL personal page link'], row['Status'], row['Payment']))

        # 2. download photo
        pic_id = row['Profile picture']
        pic_id = pic_id.split("id=",1)[1]
        img_name = row['First name'] + '_' + row['Last name'] + '.png'
        download_file_from_google_drive(pic_id, photo_path + img_name)

        # 3. generate member page
        generateMemberPage( row['First name'],  row['Last name'], row['Status'],  validities[index], 'img/' + img_name)

        # 4. send QR code
        base_link = 'https://clubmontagne.github.io/members/'
        generateQR(base_link + row['First name'] + '_' + row['Last name'])

        # 5. send QR code to the email
        try:
            send_email(row['Email Address'])
        except:
            wrong_emails.append(row['Email Address'])

    print(wrong_emails)

    # df['validity'] = validities
    # df.to_csv('test.csv')

# specify the excel to process and the member photo path
# 1. verify if the member status is valid
# 2. download the member photo to photo_path
# 3. store the QR code
if __name__ == "__main__":
    info_path = sys.argv[1]
    photo_path = sys.argv[2]
    process_info(info_path, photo_path)
