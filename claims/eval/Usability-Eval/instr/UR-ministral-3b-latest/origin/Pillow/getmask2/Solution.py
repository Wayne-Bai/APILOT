
from PIL import Image, ImageDraw, ImageFont

def create_bitmap(text, width, height, font_path, bg_color=(255, 255, 255), text_color=(0, 0, 0)):
    # Create a new image with the specified dimensions.
    image = Image.new('RGB', (width, height), bg_color)

    # Create a drawing context on the image.
    draw = ImageDraw.Draw(image)

    # Load the font file from the specified path.
    font = ImageFont.truetype(font_path, size=24)

    # Calculate the text bounding box.
    text_bbox = draw.textbbox((0, 0), text, font=font)

    # Draw the text on the image.
    draw.text((text_bbox[0], text_bbox[1]), text, font=font, fill=text_color)

    # Save or display the image as per requirement.
    # image.save('bitmap.png')  # Uncomment this line to save the bitmap
    # image.show()  # Uncomment this line to display the bitmap

    return image

# Using the function to create a bitmap for the text 'Hello, World!'
bitmap = create_bitmap('Hello, World!', 200, 150, 'arial.ttf')
bitmap.show()
