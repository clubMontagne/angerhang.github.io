# Monbers
Essentially, the QR code is made off each github site where each member will have his own page. The QR code leads directly to this particular page.

## Dependencies
Python 3.0+
pyqrcode
selenium and its driver for getting the page source and member verification

## Prepare the data
After download the data from the google drive in the clubMontagne2018@gmail.com account, one will need to add tow columns into the csv, 'Payment' and 'Email_sent'. The csv is passed to the verifyStatus script as an argument in the script.

## How to setup env
```
source env/bin/activate
```

## How to run the script 
```
python verifyStatus PATH_MEMBER_INFO PATH_PHOTO
```
`PATH_PHOTO` is where the members' photos should be stored. 

## End-to-end member system in nutshell
1. Members sign up using Google Form:
Information to be collected 
   * First name and last name
   * Email address to receive the QR code 
   * Photo 
   * Student page to verify 
   
2. Download the member info file (csv) and the photos 
to the membership system. (manual step)
    * Might need to rename the photo files or 
    specify the names format.
    * Might need to reformat the photo sizes or 
    specify the required photo size.

3. Check the student status and write to member info file.

4. Generate the member pages and make them live.

5. Send the QR code to the members.

6. Upload the csv file to the club Google drive which should be located at `Member ID/members.csv`. Make sure not to replace the existing members.csv as it is updated manually by other people who someone pays for the membership fees. One needs to sync this csv in the Google drive and the one is the member system. Currently this automation process is not being done but should be straightforward to sync in Numbers or Excel by hand.

## Contact 
Please you need help with anything or spot any mistakes. Send an email to: angerhangy@gmail.com

