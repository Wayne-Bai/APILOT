from PIL import Image, ImageDraw, ImageFont

def create_bitmap_for_text(text, font_size, font_color, background_color):
    # Create a new image with white background
    width, height = 800, 500
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate the text size
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the position to center the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=font_color)

    return image

# Example usage
bitmap = create_bitmap_for_text("Hello, Pillow!", 100, "white", "black")
bitmap.show()
