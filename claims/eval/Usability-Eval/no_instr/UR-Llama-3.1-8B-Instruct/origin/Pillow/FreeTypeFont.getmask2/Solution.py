# Import the necessary libraries
from PIL import Image, ImageDraw, ImageFont

# Function to create a bitmap for the text
def create_bitmap(text, font_size, output_filename):
    """
    Creates a bitmap for the given text using the specified font size and saves it as an image.

    Args:
        text (str): The text to be displayed on the bitmap.
        font_size (int): The size of the font to be used.
        output_filename (str): The filename to save the output image.

    Returns:
        None
    """

    # Specify the font type (in this case, a sans-serif font)
    font_name = 'arial.ttf'  # You can replace this with your preferred font

    # Create a new image with a white background
    img_width = 800  # Image width
    img_height = 600  # Image height
    img = Image.new('RGB', (img_width, img_height), (255, 255, 255))

    # Create a drawing context
    d = ImageDraw.Draw(img)

    # Set the font
    font = ImageFont.truetype(font_name, font_size)

    # Get the font's size information
    text_width, text_height = font.getsize(text)

    # Calculate the coordinates for drawing the text to center it on the image
    x = (img_width - text_width) / 2
    y = (img_height - text_height) / 2

    # Draw the text on the image
    d.text((x, y), text, font=font, fill=(0, 0, 0))  # Text color: black

    # Save the image to a file
    img.save(output_filename)

# Usage
create_bitmap('Hello, World!', 42, 'output.png')
