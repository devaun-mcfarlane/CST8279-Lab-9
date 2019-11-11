from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar
from gfxhat import backlight

myDict = {}


def generate_dictionary():

    with open('font3.txt', 'r') as f:
        stripped = (line.strip() for line in f)
        for line in stripped:
            value, key = line.split(",")
            myDict[key] = value


generate_dictionary()
print(myDict)


def display_character():
    ch = input("Enter a character: ")
    x = int(input("Enter an x coordinate: "))
    y = int(input("Enter a y coordinate: "))
    if ch in myDict:
        lcd.clear()
        width, height = lcd.dimensions()
        image = Image.new('P', (width, height))
        draw = ImageDraw.Draw(image)
        font =  ImageFont.truetype(fonts.AmaticSCBold, 12)
        w, h = font.getsize(ch)
        draw.text((x,y), ch, 1 , font)
        for x1 in range(x, x + w):
            for y1 in range(y, y+h):
                pixel = image.getpixel((x1,y1))
                lcd.set_pixel(x1,y1,pixel)
        lcd.show()

    else:
        print("Chosen Character not Present in Dictionary")



