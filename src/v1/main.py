from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/Poppins/Poppins-BoldItalic.ttf', 140)
FONT_FILE2 = ImageFont.truetype(r'font/Poppins/Poppins-Bold.ttf', 140)
FONT_COLOR = "#FFFFFF"
IMAGE_SOURCE = r'template_final.png'


template = Image.open(IMAGE_SOURCE)
WIDTH, HEIGHT = template.size

def make_certificates(name, counter, mod_text):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(IMAGE_SOURCE)
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    lines = name.split("|")
    name_width, name_height = draw.textsize(lines[0], font=FONT_FILE)
    what_width, what_height = draw.textsize(lines[1], font=FONT_FILE)
    mod_width, mod_height = draw.textsize(mod_text, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - what_height - name_height - mod_height) / 2 - 100), lines[0], fill=FONT_COLOR, font=FONT_FILE)
    draw.text(((WIDTH - mod_width) / 2, (HEIGHT - what_height - mod_height) / 2 + 50), mod_text, fill=FONT_COLOR, font=FONT_FILE2)
    draw.text(((WIDTH - what_width) / 2, (HEIGHT - what_height) / 2 + 225), lines[1], fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + str(counter) + "-" + name.split("|")[-1].strip() +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":
    counter = 1
    with open('names.txt') as fh:
        names = fh.readlines()
        for name in names:
            make_certificates(name, counter, "For creating a project that was the")
            counter += 1

        print(len(names), "certificates done.")

