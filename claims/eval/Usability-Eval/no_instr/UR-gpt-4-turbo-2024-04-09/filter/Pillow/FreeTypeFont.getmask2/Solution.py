from PIL import Image, ImageDraw, ImageFont

def create_text_bitmap(text, font_path, font_size, image_path):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Create a new image with white background
    image = Image.new('RGB', (800, 200), 'white')
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Calculate text width and height
    text_width, text_height = draw.textsize(text, font=font)
    
    # Calculate the position at which to draw the text
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2
    
    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    
    # Save the image to a file
    image.save(image_path)

# Usage example:
# Replace 'arial.ttf' with the path to a font file on your system
create_text_bitmap("Hello, World!", "arial.ttf", 48, "output_image.png")
