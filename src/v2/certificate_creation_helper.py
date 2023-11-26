from PIL import Image, ImageFont, ImageDraw

# Function to create a certificate, and store it as a .png file.
def make_certificate(
        name, counter, mod_text, 
        font_color, image_source, font_file_path,
        image_folder, log_file_path
    ):

    template = Image.open(image_source)
    width, height = template.size
    font_file = ImageFont.truetype(font_file_path, 70)

    log = open(log_file_path, "a")

    image_source = Image.open(image_source)
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    lines = name.split(",")
    lines = [line.strip() for line in lines]
    if len(lines[4].strip()) == 0 or lines[4].strip().lower().startswith("team") and len(lines[4].strip()) == 4:
        full_string = lines[1] + " " + lines[2]
    elif lines[4].strip().lower().startswith("team"):
        full_string = lines[1] + " " + lines[2] + mod_text + "\"" + lines[4][5:] + "\""
    else:
        full_string = lines[1] + " " + lines[2] + "," + mod_text + "\"" + lines[4] + "\""

    name_width, name_height = draw.textsize(full_string, font=font_file)
    # what_width, what_height = draw.textsize(lines[4], font=FONT_FILE)
    # mod_width, mod_height = draw.textsize(mod_text, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((width - name_width) / 2, (height - name_height) / 2 - 50), full_string, fill=font_color, font=font_file)
    # draw.text(((WIDTH - mod_width) / 2, (HEIGHT - what_height - mod_height) / 2 + 50), mod_text, fill=FONT_COLOR, font=FONT_FILE2)
    # draw.text(((WIDTH - what_width) / 2, (HEIGHT - what_height) / 2 + 225), lines[4], fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save(image_folder + str(counter) + "-" + name.split(",")[3].strip() +".png")
    print('Saving Certificate of:', name, file=log)
    log.close()

