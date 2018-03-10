# Monbers
## Dependencies
Python 3.0+
pyqrcode
selenium and its driver for getting the page source and member verification


## How to setup env
```
source env/bin/activate
```

## How to run the script 
```
python verifyStatus PATH_MEMBER_INFO PATH_PHOTO_PATH
```


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


