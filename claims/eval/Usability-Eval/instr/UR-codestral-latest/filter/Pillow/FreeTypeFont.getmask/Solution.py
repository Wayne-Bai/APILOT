from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_path, font_size, image_size, fill_color, background_color):
    # Creating a new image object with the specified background color
    img = Image.new('RGB', image_size, background_color)

    # Getting a drawing context on the image
    draw = ImageDraw.Draw(img)

    # Specifying the font
    font = ImageFont.truetype(font_path, font_size)

    # Drawing the text on the image
    draw.text((10, 10), text, fill=fill_color, font=font)

    return img

# Using the function
img = text_to_image("Hello, World!", "arial.ttf", 24, (200, 50), "black", "white")

# Saving the final image
img.save('text_image.png')
