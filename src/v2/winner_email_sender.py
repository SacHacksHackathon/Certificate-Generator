import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

names = dict()
with open("names.txt") as fh:
    lines = fh.readlines()
    for line in lines:
        line = line.strip()
        dets = [x.strip() for x in line.split("|")]
        if not dets[2] in names:
            names[dets[2]] = [dets[0], dets[1]]
        else:
            curr = names[dets[2]]
            curr.append(dets[1])
            names[dets[2]] = curr

pic_list = os.listdir("./winner-out")

processed = dict()

for pic in pic_list:
    if not pic in processed:
        processed[pic] = 1
        current_email = pic.split("-")[-1].split(".png")[0]
        subject = "Congrats on your win at SacHacks IV!"
        print(current_email)

        if len(names[current_email]) == 2:
            body = "Hey " + names[current_email][0] + "!\n" +\
                    "Hope this email finds you well.\n" +\
                    "We at the SacHacks team wanted to congratulate you on creating a project that was the " + names[current_email][1] + " at SacHacks IV, and share this official certificate that you can host on a cloud platform of your choice and attach to your portfolio websites.\n" +\
                    "\n\n" +\
                    "Thank you once again for taking part in SacHacks IV and making the best use of all the opportunities available. We are looking forward to seeing you at our next event!\n" +\
                    "\n\n" +\
                    "P.S. If you are having some trouble opening the attachment, try using Gmail on your browser.\n\n" +\
                    "\nAlso, we are resending this certificate as some people didn't receive it the first time we sent it. If you received our initial email, you can ignore this one." +\
                    "Warm Regards,\n" +\
                    "SacHacks Team"
        else:
            congrats_line = " and ".join(names[current_email][1:])
            body = "Hey " + names[current_email][0] + "!\n" +\
                    "Hope this email finds you well.\n" +\
                    "We at the SacHacks team wanted to congratulate you on creating a project that was the " + congrats_line + " at SacHacks IV, and share these official certificates that you can host on a cloud platform of your choice and attach to your portfolio websites.\n" +\
                    "\n\n" +\
                    "Thank you once again for taking part in SacHacks IV and making the best use of all the opportunities available. We are looking forward to seeing you at our next event!\n" +\
                    "\n\n" +\
                    "P.S. If you are having some trouble opening the attachment, try using Gmail on your browser.\n\n" +\
                    "Warm Regards,\n" +\
                    "SacHacks Team"
        body += "\n\n"
        
        sender_email = sender_email = os.environ["EMAIL"]
        password = os.environ["EMAIL_PASSWORD"]
        receiver_email = os.environ["EMAIL"] # change to current_email
        
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = current_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filenames = ["./out/" + p for p in os.listdir("./out") if p.split("-")[-1] == pic.split("-")[-1]]  # In same directory as script
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

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)