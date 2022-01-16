from PIL import Image

img = Image.open("GreenApple.jpg")
width, height = img.size

def getPixelColor(image, x, y):
    r,g,b = image.getpixel((x, y))
    print("R: {}, G: {}, B: {}".format(r,g,b))

def changeToNegative(image):
    for y in range(height):
        for x in range(width):
            r,g,b = image.getpixel((x, y))
            image.putpixel((x, y), (255-r,255-g,255-b))
    image.show()

def makeItGray(image):
    for y in range(height):
        for x in range(width):
            r,g,b = image.getpixel((x, y))
            grayColor = (r+g+b)//3
            image.putpixel((x, y), (grayColor, grayColor, grayColor))
    image.show()

def halfNegativeHalfGray(image):
    width1, height1 = image.size
    imgHalf = height1//2
    for y in range(height):
        for x in range(width):
            r,g,b = image.getpixel((x, y))
            if y < imgHalf:
                image.putpixel((x, y), (255-r, 255-g, 255-b))
            else:
                grayColor = (r+g+b)//3
                image.putpixel((x, y), (grayColor, grayColor, grayColor))
    image.show()

def canalChange(image):
    for y in range(height):
        for x in range(width):
            r,g,b = image.getpixel((x, y))
            image.putpixel((x, y), (g, b, r))
    image.show()

def keepGreen(image):
    for y in range(height):
        for x in range(width):
            r,g,b = image.getpixel((x, y))
            image.putpixel((x, y), (b, g, r))
    image.show()

def bluePixelOntheLeft(image):
    image.putpixel((100, 250), (0, 0, 255))
    image.show()

def redPixelOntheCenter(image):
    image.putpixel((250, 250), (255, 0, 0))
    image.show()
    image.save("GreenAppleWithRedPixel.jpeg", "jpeg")

