# Certificate-Generator v2.0
A set of scripts to generate and email participation and winner certificates


# Using the program
## How to run the program
1. Make sure that the csv of certificate receivers follows the format shown below.
2. Edit `lines 30-35` in `src/v2/certificate_creation_helper.py` to pick the location where each customized text you want to put in a certificate goes. This should be the only code change needed each time you use this script. Refer to the surround code and the Python documentation for [Pillow](https://pillow.readthedocs.io/en/stable/).
3. Place the CSV file and the image template for the certificate as described in the file structure. The script should work even if you don't, but it is important for the sake of consistency. Quick TLDR:
      - `certificate-templates/SacHacks-[roman numeral for current iteration]` - Certificate Template
      - `input-data/SacHacks-[roman numeral for current iteration]` - Input CSV data
      - Read through the whole section about file structure before you use the script. It has a lot of tips you would find useful.
4. Make sure to first test both parts of the script individually, and then together for a small subset of the certificates. When testing the email functionality, send it to a few members of your team to ensure that it appears as expected in a variety of devices.
5. Create a JSON file using the format shown below to provide the required input. 
6. Now run the script: `python3 main.py path/to/input/jsonfile.json`
     - First run it with the `should_send_certificates` flag set to `false` in the input JSON file - make sure all the certificates where generated properly.
     - Manually fix any rows with broken data and run the script again to generate the certificates for them.
     - Once the certificates are verified to be good to send, set the `should_create_certificates` flag to `false` and the `should_send_certificates` flag to true to send those certificates without regenerating them.
     - I would highly recommend you to do this process in small batches for the sake of your mental health.  


## Example input for the program
(Put the following in a JSON file and provide the path to that file to `main.py` as a parameter)
```json
{
  "csv_file_path": "path/to/csv/file", // Where the CSV of certificate receivers is
  "certificate_template_path": "path/to/certificate/template", // Where the certificate template is
  "font_file_path": "path/to/font/file", // Where the .tiff font file is
  "font_color": "white", // eg: "white", "black" --> pick the font color
  "font_size": 70, // pick the size of the font
  "images_folder_path": "path/to/images/folder", // Where the generated certificates should be stored
  "should_create_certificates": true, // Should certificates be created? Set to false if the certificates have already been made.
  "should_send_certificates": true, // Should the certificates be sent? Set to false if you only want the certificates to be created and not sent to anyone yet.
  "email": "example@example.com", // The email the certificates should be sent from
  "password": "password123", // Password of the above email
  "subject": "Certificate Subject", // Subject of email sent to certificate receivers
  "body": "Certificate Body", // Body of the email sent --> Refer to the Email Personalization Tags section below for more info.
  "log_file_path": "path/to/log/file" // Where should the logs be stored?
}
```

## Expected CSV format
Entry Number | First Name | Last Name | Email | Team Name | Feat |
|   ------   |    ---     |    ---    |   --  |    ---    |  --  |
1            | Adityaa    | Ravi      |       | SacHacks  | for organizing SacHacks IV and V     

## Email Personalization Tags

Tag                   | What
-----------------     | ------------------                       
`{first_name}`        | Full name of the participant
`{last_name}`         | Last name of the participant
`{team_name}`         | Team name of the participant
`{feat}`              | Why we are giving this certificate to the participant 
 
**`{feat}` Example:**
"for participating", "for being the second runner up in the Best Local Hack track", etc.

-------------------------------------------------------------------------------------------

# Software Development Notes


## Some Useful Links:
- Python documentation for [Pillow](https://pillow.readthedocs.io/en/stable/)
- A .ttf (True-Type Font) file like [this](/font), can be downloaded from [here](https://www.google.com/search?q=download+.ttf+fonts). When creating the designs for the certificates, please make sure that a .tiff file for the fonts used can be easily found online.

## Code File Structure

*`src/`*
- `src/v2`
  - This folder has the code for CertificateGenerator v2 -- Currently the latest version
  - `main.py` - Main method for the script. Run this file to run the script.
  - `certificate_creation_helper.py` - Helper method to create each of the certificates.
  - `certificate_email_helper.py` - Helper method to send each certificates to the respective receiver.

- `src/v1/`
  - Old code used during SacHacks IV. This was pretty much just quickly cobbled together--so don't have a lot of expectations.
  - This won't work with the current file structure. Only use this as an example during future development and for not much else.  


## Suggested File Structure and tips for usage
You are not required to follow the following file structure for using the script, but doing so will help you a lot with staying organized... Especially considering that you will be generating hundreds upon hundreds of certificates and emailing them out. This section also has some tips regarding using this script that you might find very useful.


*`certificate-templates/SacHacks-[roman numeral for current iteration]`*
- Example: `certificate-templates/SacHacks-V`
- Use this to contain both the template file for both the participation and winner certificates
- Make sure that the file sizes are small (< 1 MB), as that significantly speeds up the scripts for both image processing and for emailing.

*`fonts/`*
- Put all your fonts here

*`generated-certificates/SacHacks-[roman numeral for current iteration]`*
- Example: `generated-certificates/SacHacks-V`
- `generated-certificates/SacHacks-[rn]/participation-automatic`
  - Automatically generated participation certificates for all participants
- `generated-certificates/SacHacks-[rn]/winner-automatic`
- Automatically generated certificates for all winners
- `generated-certificates/SacHacks-[rn]/participation-testing` 
  - Participation certificates generated using provided testing data
- `generated-certificates/SacHacks-[rn]/winner-testing`
  - Winner certificates generated using provided testing data 
- `generated-certificates/SacHacks-[rn]/participation-manual` (Hope you don't need this :))
  - Certificates generated using manually fixed and validated data
- `generated-certificates/SacHacks-[rn]/winner-manual` (Hope you don't need this:))
  - Certificates generated using manually fixed and validated data

(Replace `[rn]` with the roman numeral corresponding to the current SacHacks iteration)


*`input-data/SacHacks-[roman numeral for current iteration]`*
- Example: `input-data/SacHacks-V`
- Files:
  - `manually_processed.csv`
    - Manually fixed data (Hope you don't need this :))
  - `participation_cert.csv`
    - Participant data to use for generating the certificates and sending them
  - `*test*`
    - Test data to make sure that the certificates are properly generated and sent before using the script to actually send them to participants


## Opportunities For Improvement:
- Create a simple GUI to allow users to easily figure out the location of the text and the font size to use.
  - Refactor the application into a web-server to allow us to create a react/next.js application that utilizes this service 
- Assign unique identification IDs to each certificate and store them in google sheets (or a database) to allow certificate validation by a third party--either through a react/next.js application we create or by at least asking the SacHacks team to do it as an MVP.

-------------------------------------------------------------------------------------------
# Credit:
[Adityaa Ravi](https://github.com/adityaaravi) - President at SacHacks (SacHacks IV and V)   
