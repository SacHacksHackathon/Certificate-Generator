from PIL import Image, ImageFont, ImageDraw

# Function to create a certificate, and store it as a .png file.
def make_certificate(
        name, counter, mod_text, 
        font_color, font_size, font_file_path,
        image_source, image_folder, 
        log_file_path
    ):

    template = Image.open(image_source)
    width, height = template.size
    font_file = ImageFont.truetype(font_file_path, font_size)

    log = open(log_file_path, "a")

    image_source = Image.open(image_source)
    draw = ImageDraw.Draw(image_source)

    lines = name.split(",")
    full_name = lines[1] + " " + lines[2]
    feat = lines[5]
    
    # Participation:
    # name_width, name_height = draw.textsize(full_name, font=font_file)
    # draw.text(((width - name_width) / 2, (height - name_height) / 2 + 77), full_name, fill=font_color, font=font_file)

    # Winner:
    name_width, name_height = draw.textsize(full_name, font=font_file)
    feat_width, feat_height = draw.textsize(feat, font=font_file)

    draw.text(((width - name_width) / 2, (height - feat_height - name_height) / 2 + 25), full_name, fill=font_color, font=font_file)
    draw.text(((width - feat_width) / 2, (height - feat_height) / 2 + 150), feat, fill=font_color, font=font_file)

    # lines = name.split(",")
    # lines = [line.strip() for line in lines]
    # if len(lines[4].strip()) == 0 or lines[4].strip().lower().startswith("team") and len(lines[4].strip()) == 4:
    #     full_string = lines[1] + " " + lines[2]
    # elif lines[4].strip().lower().startswith("team"):
    #     full_string = lines[1] + " " + lines[2] + mod_text + "\"" + lines[4][5:] + "\""
    # else:
    #     full_string = lines[1] + " " + lines[2] + "," + mod_text + "\"" + lines[4] + "\""

    # Saving the certificates in a different directory.
    image_source.save(image_folder + "/" + str(counter) + "-" + name.split(",")[3].strip() +".png")
    print('Saving Certificate of:', name, file=log)
    log.close()

