from PIL import Image, ImageDraw, ImageFont

def create_bitmap(text, font_size=24, font_name='arial.ttf', output_file='bitmap.png'):
    """
    Create a bitmap for the given text.

    Args:
        text (str): The text to render as a bitmap.
        font_size (int): The font size to use. Defaults to 24.
        font_name (str): The font name to use. Defaults to 'arial.ttf'.
        output_file (str): The file name to save the bitmap as. Defaults to 'bitmap.png'.

    Returns:
        None
    """

    # Calculate the width and height required for the text
    font = ImageFont.truetype(font_name, font_size)
    width, height = font.getsize(text)

    # Add a small padding around the text
    width += 10
    height += 10

    # Create a new image with white background
    img = Image.new('RGB', (width, height), (255, 255, 255))

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Render the text at the center of the image
    draw.text((5, 5), text, font=font, fill=(0, 0, 0))

    # Save the image to the output file
    img.save(output_file)

# Example usage
create_bitmap('Hello, world!')
