import time
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

names = dict()
with open('part_cert_list.csv') as fh:
    lines = fh.readlines()
    for line in lines:
        line = line.strip()
        dets = [x.strip() for x in line.split(",")]
        names[dets[3]] = [dets[1] + " " + dets[2], dets[4]]

dire = "./out"
pic_list = os.listdir(dire)

sender_email = os.environ["EMAIL"]
password = os.environ["EMAIL_PASSWORD"]

       
# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    for pic in pic_list:
        try: 
            current_email = pic.split("-")[-1].split(".png")[0]
            subject = "Thanks for Participating in SacHacks IV!"
            print(current_email)

            body = "Hey " + names[current_email][0] + "!\n" +\
                "Hope this email finds you well.\n\n" +\
                "We wanted to share this official participation certificate that you can host on a cloud platform of your choice and attach to your portfolio websites." +\
                "\n" +\
                "Thank you once again for taking part in SacHacks IV and making the best use of all the opportunities available. We are looking forward to seeing you at our next event!" +\
                "\n\n" + \
                "We are hosting SacHacks to provide you a platform to build and showcase your ideas, so your opinions are quite valuable to us. If you have any feedback, suggestions, or questions, we would greatly appreciate it if you could share it by emailing us at contact@sachacks.io." +\
                "\n\n" +\
                "P.S. If you are having some trouble opening the attachment, try using Gmail on your browser. If you continue to have issues accessing the certificate, please email us at contact@sachacks.io." +\
                "\nAlso, we are resending this certificate as some people didn't receive it the first time we sent it. If you recevied our initial email, you can ignore this one." +\
                "\n\n" +\
                "Warm Regards,\n" +\
                "SacHacks Team"
            
            body += "\n\n"
            
            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = current_email
            message["Subject"] = subject
            receiver_email = current_email
            # message["Bcc"] = current_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            filenames = [dire + "/" + p for p in os.listdir(dire) if p.split("-")[-1] == pic.split("-")[-1]]  # In same directory as script
            #print(filenames)
            for filename in filenames:
                # Open PDF file in binary mode
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
            server.sendmail(sender_email, receiver_email, text)
        except Exception as err:
            print("ERROR while sending:", pic, err)