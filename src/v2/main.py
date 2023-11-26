import sys
import json

# importing helper functions
from certificate_creation_helper import make_certificate
from certificate_email_helper import send_certificates

def main():
    if len(sys.argv) < 2:
        print("Please provide the path to the JSON file as a command line argument.")
        return

    json_file_path = sys.argv[1]
    data = json.load(open(json_file_path, "r"))

    csv_file_path = data.get("csv_file_path")
    certificate_template_path = data.get("certificate_template_path")
    font_file_path = data.get("font_file_path")
    font_color = data.get("font_color")
    images_folder_path = data.get("images_folder_path")
    should_create_certificates = data.get("should_create_certificates")
    should_send_certificates = data.get("should_send_certificates")
    email = data.get("email")
    password = data.get("password")
    subject = data.get("subject")
    body = data.get("body")
    log_file_path = data.get("log_file_path")

    log = open(log_file_path, "a")
    print("Starting...\n" + "_"*10, file=log)

    # If the JSON file does not contain the required fields, return.
    if not csv_file_path or not images_folder_path or \
       not should_send_certificates or not email or not password or \
       not subject or not body or not log_file_path or not certificate_template_path\
       or not font_file_path or not font_color:
        print("Please provide all the required fields in the JSON file.", file=log)
        return
    

    if should_create_certificates:
        print("Creating certificates...", file=log)
        counter = 1
        with open(csv_file_path) as fh:
            names = fh.readlines()
            for name in names:
                if counter != 1:
                    make_certificate(
                        name, counter, " from Team ", 
                        font_color, certificate_template_path, font_file_path,
                        images_folder_path, log_file_path
                    )
                counter += 1

            print(len(names), "certificates done.", file=log)
    
    if should_send_certificates:
        print("Sending certificates...", file=log)
        send_certificates(csv_file_path, images_folder_path, email, password, subject, body, log_file_path)
        print("Certificates sent.", file=log)
        
    print("Done.", file=log)
    print("_"*10, file=log)
    log.close()


if __name__ == "__main__":
    main()
