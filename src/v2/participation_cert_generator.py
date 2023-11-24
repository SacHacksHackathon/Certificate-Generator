from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/Poppins/Poppins-BoldItalic.ttf', 70)
FONT_FILE2 = ImageFont.truetype(r'font/Poppins/Poppins-Bold.ttf', 70)
FONT_COLOR = "#FFFFFF"
IMAGE_SOURCE = r'part_cert_compressed.png'


template = Image.open(IMAGE_SOURCE)
WIDTH, HEIGHT = template.size

def make_certificates(name, counter, mod_text):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(IMAGE_SOURCE)
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

    name_width, name_height = draw.textsize(full_string, font=FONT_FILE)
    # what_width, what_height = draw.textsize(lines[4], font=FONT_FILE)
    # mod_width, mod_height = draw.textsize(mod_text, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 50), full_string, fill=FONT_COLOR, font=FONT_FILE)
    # draw.text(((WIDTH - mod_width) / 2, (HEIGHT - what_height - mod_height) / 2 + 50), mod_text, fill=FONT_COLOR, font=FONT_FILE2)
    # draw.text(((WIDTH - what_width) / 2, (HEIGHT - what_height) / 2 + 225), lines[4], fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out-err/" + str(counter) + "-" + name.split(",")[3].strip() +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":
    counter = 1
    with open('part_cert_test.csv') as fh:
        names = fh.readlines()
        for name in names:
            if counter != 1:
                make_certificates(name, counter, " from Team ")
            counter += 1

        print(len(names), "certificates done.")


