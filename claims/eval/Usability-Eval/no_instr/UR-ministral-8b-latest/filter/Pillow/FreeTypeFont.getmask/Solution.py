from PIL import ImageDraw, ImageFont

def create_text_bitmap(text, font_path, width, height):
    # Load the font
    font = ImageFont.truetype(font_path, size=20)

    # Create a blank image with black background
    image = Image.new("RGBA", (width, height), (0, 0, 0, 255))

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Define the position to write the text
    text_position = ((width - font.getsize(text)[0]) // 2, (height - font.getsize(text)[1]) // 2)

    # Write the text on the image
    draw.text(text_position, text, fill="white", font=font)

    return image

# Example usage
text = "Hello, Pillow!"
font_path = "arial.ttf"  # Replace with the path to your font file
bitmap = create_text_bitmap(text, font_path, 800, 600)
bitmap.show()
