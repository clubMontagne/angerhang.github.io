import urllib.request
import csv
import qrcode
import webbrowser

def verifyMember(p_link):
    """
    :param p_link: the link of the student profile
    :return: true if the page is valid and contains student
    otherwise no
    """
    try:
        f = urllib.request.urlopen(p_link)
        web_page = f.read()

        if b'student' in web_page:
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

    # Create an image from the QR Code instance
    img = qr.make_image()
    img.show()
    img.save("image.jpg")

f = open('../data/test1.csv')
csv_f = csv.reader(f)

confirmations = []

for row in csv_f:
    # column 1 as the member status
    row[1] = verifyMember(row[4])
    # colum 5 as the profile url

    # column 6 is the generated
    print (row)

generateQR('han')
