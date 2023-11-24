# Certificate-Generator v2.0
A set of scripts to generate and email participation and winner certificates

--------------------------
## Some useful links:
- Python documentation for [Pillow](https://pillow.readthedocs.io/en/stable/)
- A .ttf (True-Type Font) file like [this](/font), can be downloaded from [here](https://www.google.com/search?q=download+.ttf+fonts). When creating the designs for the certificates, please make sure that a .tiff file for the fonts used can be easily found online.
--------------------------
## File Structure

*`certificate-templates/SacHacks-[roman numeral for current iteration]`*
- Example: `certificate-templates/SacHacks-V`
- Contains the template file for both the participation and winner certificates
- Make sure that the file sizes are small (< 1 MB), as that significantly speeds up the scripts for both image processing and for emailing.
--------------------------
*`fonts/`*
- Put all your fonts here

--------------------------
*`generated-certificates/SacHacks-[roman numeral for current iteration]`*
- Example: `generated-certificates/SacHacks-V`
- Guaranteed:
  - `generated-certificates/SacHacks-[rn]/participation-automatic`
    - Automatically generated participation certificates for all participants
  - `generated-certificates/SacHacks-[rn]/winner-automatic`
    - Automatically generated certificates for all winners
- Optional:
  - `generated-certificates/SacHacks-[rn]/participation-testing` (Optional, but recommended)
    - Participation certificates generated using provided testing data (use the `test` flag) 
  - `generated-certificates/SacHacks-[rn]/winner-testing` (Optional, but recommended)
    - Winner certificates generated using provided testing data (use the `test` flag) 
  - `generated-certificates/SacHacks-[rn]/participation-manual` (Optional, Hope you don't need this)
    - Certificates generated using manually fixed and validated data
  - `generated-certificates/SacHacks-[rn]/winner-manual` (Optional, Hope you don't need this)
    - Certificates generated using manually fixed and validated data

(Replace `[rn]` with the roman numeral corresponding to the current SacHacks iteration)

--------------------------
*`input-data/SacHacks-[roman numeral for current iteration]`*
- Example: `input-data/SacHacks-V`
- Files:
  - `manually_processed.csv`
    - Manually fixed data
  - `participation_cert.csv`
    - Participant data to use for generating the certificates and sending them
  - `*test*` (Optional, but recommended--Obviously)
    - Test data to make sure that the certificates are properly generated and sent before using the script to actually send them to participants

--------------------------
*`src/`*
- `src/v2`
  - This folder has the code for CertificateGenerator v2

- `src/v1/`
  - Old code used during SacHacks IV. This was pretty much just quickly cobbled together--so don't have a lot of expectations.
  - This won't work with the current file structure. Only use this as an example during future development and for not much else.  
--------------------------
## Opportunities for improvement:
- Create a simple GUI to allow users to easily figure out the location of the text and the font size to use.
  - Refactor the application into a web-server to allow us to create a react/next.js application that utilizes this service 
- Assign unique identification IDs to each certificate and store them in google sheets (or a database) to allow certificate validation by a third party--either through a react/next.js application we create or by at least asking the SacHacks team to do it as an MVP.

--------------------------
## Credit:
The image processing parts of these scripts are based on the work of [Tushar Nankani](https://raw.githubusercontent.com/tusharnankani/CertificateGenerator/main/main.py). [Adityaa Ravi](https://github.com/adityaaravi) modified that script to suit the needs of SacHacks, and made the rest of the scripts provided in this repository including the ones for processing participant data and sending emails. He also   
