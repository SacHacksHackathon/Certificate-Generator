import time
import email, smtplib, ssl
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_certificates(csv_file_path, images_folder_path, email, password, subject, main_body, log_file_path):
    log = open(log_file_path, "a")
    names = dict()
    with open(csv_file_path) as fh:
        lines = fh.readlines()
        for line in lines:
            line = line.strip()
            details = [x.strip() for x in line.split(",")]
            # names[email] = [full name, team_name, feat]
            # where feat is what we are giving this certificate to the participant for:
            # Example: "for participating", "for being the second runner up in the Best Local Hack track", etc.
            names[details[3]] = [details[1] + " " + details[2], details[4]]

    # get a list of all the certificates generated earlier
    pic_list = os.listdir(images_folder_path)
        
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Logging into gmail. NOTE: Make sure you have enabled less secure apps on your gmail account.
        server.login(email, password)
        
        for pic in pic_list:
            try: 
                current_email = pic.split("-")[-1].split(".png")[0]
                subject = "Thanks for Participating in SacHacks IV!"
                print(current_email)

                # Replace the following tags with the appropriate values:
                # {first_name} - Full name of the participant
                # {last_name} - Last name of the participant
                # {team_name} - Team name of the participant
                # {feat} - Why we are giving this certificate to the participant: 
                #          "for participating", "for being the second runner up in the Best Local Hack track", etc.

                body = main_body.format(
                    first_name=names[current_email][0].split(" ")[0],
                    last_name=names[current_email][0].split(" ")[1],
                    team_name=names[current_email][1],
                    feat=names[current_email][2],
                )
                
                # Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = email
                message["To"] = current_email
                message["Subject"] = subject
                receiver_email = current_email
                # message["Bcc"] = current_email  # Recommended for mass emails

                # Add body to email
                message.attach(MIMEText(body, "plain"))

                filenames = [images_folder_path + "/" + p for p in os.listdir(images_folder_path) if p.split("-")[-1] == pic.split("-")[-1]]  # In same directory as script
                #print(filenames)
                for filename in filenames:
                    # Open the png file in binary mode
                    with open(filename, "rb") as attachment:
                        # Add file as application/octet-stream
                        # Email client can usually download this automatically as attachment
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())

                    # Encode file in ASCII characters to send by email    
                    encoders.encode_base64(part)

                    # Add header as key/value pair to attachment part
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={names[current_email][0]}-{names[current_email][1]}-certificate.png",
                    )

                    # Add attachment to message and convert message to string
                    message.attach(part)

                text = message.as_string()
                # sleep for 1 second to prevent emails getting missed.
                time.sleep(1)
                server.sendmail(email, receiver_email, text)
            except Exception as err:
                print("ERROR while sending:", pic, err, file=log)
    
    log.close()