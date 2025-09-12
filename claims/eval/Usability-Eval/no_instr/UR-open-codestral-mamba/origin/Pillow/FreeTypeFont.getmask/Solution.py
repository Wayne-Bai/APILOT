from PIL import Image, ImageDraw, ImageFont

def create_bitmap_text(text, filename='bitmap.png'):
    # create a black background
    img = Image.new("RGB", (500, 500), "black")

    # create a draw object
    draw = ImageDraw.Draw(img)

    # choose a font
    font = ImageFont.truetype("arial.ttf", 30)

    # draw the text onto the image
    draw.text((90, 90), text, font=font, fill="white")

    # save the image
    img.save(filename)

    # show the image
    img.show()

# Use the function to create the bitmap for the text
create_bitmap_text("Hello, World!")
