from PIL import Image, ImageDraw, ImageFont

def create_text_bitmap(text, font_size, font_path, text_color, bg_color):
    # Create a blank image and get a drawing context
    img = Image.new('RGB', (1, 1), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Get the size of the text
    text_width, text_height = draw.textsize(text, font)

    # Create a new image with the correct size
    img = Image.new('RGB', (text_width, text_height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Draw the text
    draw.text((0, 0), text, fill=text_color, font=font)

    return img
