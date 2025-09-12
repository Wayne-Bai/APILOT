from PIL import Image, ImageDraw, ImageFont

# Function to create a bitmap image with given text
def create_text_bitmap(text, font_path='arial.ttf', font_size=20, image_size=(200, 100), bg_color=(255, 255, 255), text_color=(0, 0, 0)):
    try:
        # Load the font
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        # If the font is not found, use a default PIL font
        font = ImageFont.load_default()

    # Create a new image with white background
    image = Image.new('RGB', image_size, bg_color)

    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)

    # Calculate text width and height
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

    # Calculate X, Y position for the text
    x = (image_size[0] - text_width) / 2
    y = (image_size[1] - text_height) / 2

    # Add text to image
    draw.text((x, y), text, font=font, fill=text_color)

    return image

# Usage example
bitmap_image = create_text_bitmap("Hello, Pillow!")
bitmap_image.show()
bitmap_image.save("text_bitmap.png")
