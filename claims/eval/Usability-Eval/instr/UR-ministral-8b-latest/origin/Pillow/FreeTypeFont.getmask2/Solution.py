from PIL import Image, ImageDraw, ImageFont

def create_text_bitmap(text, font_size=40, background_color=(255, 255, 255), text_color=(0, 0, 0)):
    # Calculate the font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Create the image with white background
    bitmap_width = len(text) * font_size
    image = Image.new("RGB", (bitmap_width, font_size), background_color)

    # Initialize the drawing library
    draw = ImageDraw.Draw(image)

    # Calculate the text size
    text_width, text_height = draw.textsize(text, font=font)

    # Draw the text
    draw.text((0, 0), text, font=font, fill=text_color)

    return image

if __name__ == "__main__":
    # Example usage
    text = "Hello, World!"
    image = create_text_bitmap(text)
    image.show()  # This will display the bitmap with the text
