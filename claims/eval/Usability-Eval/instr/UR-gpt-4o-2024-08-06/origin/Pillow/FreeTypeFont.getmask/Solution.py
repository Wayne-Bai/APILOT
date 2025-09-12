from PIL import Image, ImageDraw, ImageFont

def create_text_bitmap(text, font_path, font_size, image_size, text_position, text_color, bg_color):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Create a new image with the given background color
    image = Image.new('RGB', image_size, bg_color)
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Draw the text onto the image at the specified position
    draw.text(text_position, text, font=font, fill=text_color)
    
    return image

# Example Usage
# Define parameters for text bitmap
text = "Hello, Pillow!"
font_path = "/path/to/font.ttf"  # Update the path to your font file
font_size = 40
image_size = (300, 100)
text_position = (10, 30)
text_color = (255, 255, 255)  # White
bg_color = (0, 0, 0)  # Black

# Create the text bitmap
bitmap = create_text_bitmap(text, font_path, font_size, image_size, text_position, text_color, bg_color)

# Save the bitmap to a file
bitmap.save("text_bitmap.png")
