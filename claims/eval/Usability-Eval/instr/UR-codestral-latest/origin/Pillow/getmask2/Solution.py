from PIL import Image, ImageDraw, ImageFont

def text_to_bitmap(text, font_path=None, font_size=12, color=(0, 0, 0)):
    # Create font object with specified font, font size
    font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()

    # Measure the size of the text
    text_width, text_height = font.getsize(text)

    # Create a new image with a white background
    image = Image.new('1', (text_width, text_height), 1)

    draw = ImageDraw.Draw(image)

    # Draw the text onto the image
    draw.text((0,0), text, font=font, fill=0)

    return image

# Use the function
image = text_to_bitmap('Hello, world!')
image.save('output_image.png')
