from PIL import Image

img = Image.open("GreenApple.jpg")
width, height = img.size

def getPixelColor(image, x, y):
    r,g,b = image.getpixel((x, y))
    print("R: {}, G: {}, B: {}".format(r,g,b))