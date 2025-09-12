from PIL import Image, ImageDraw, ImageFont

def text_to_bitmap(text: str, font_size = 20, font = "arial.ttf") -> Image.Image:
    # Create a blank image
    image = Image.new("RGB", (100, 100), color = (255, 255, 255))

    # Load the font
    font = ImageFont.truetype(font, font_size)

    # Draw the text on the image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font = font, fill = 'black')

    return image

# Example usage:
image = text_to_bitmap("Hello, World!")
image.show()
