from PIL import Image, ImageDraw, ImageFont

def create_bitmap(text, font_path):
    # Create a blank image with white background
    image = Image.new("RGB", (300, 100), "white")

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype(font_path, 30)

    # Calculate the size of the text
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the position to draw the text
    x = (300 - text_width) / 2
    y = (100 - text_height) / 2

    # Draw the text
    draw.text((x, y), text, font=font)

    # Save the bitmap
    image.save("bitmap.png")

# Example usage
create_bitmap("Hello, World!", "arial.ttf")
