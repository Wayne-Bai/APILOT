from PIL import Image, ImageDraw, ImageFont

def create_bitmap(text, filename="output.bmp"):
    # Creating blank image
    image = Image.new("RGBA", (500, 100), "white")

    # Creating image object
    draw = ImageDraw.Draw(image)

    # Using a truetype font
    font = ImageFont.truetype("fonts/arial.ttf", 20)

    # Adding the text
    draw.text((10, 10), text, font=font, fill="black")

    # Saving the image
    image.save(filename)

# Using the function
create_bitmap("Hello World")
