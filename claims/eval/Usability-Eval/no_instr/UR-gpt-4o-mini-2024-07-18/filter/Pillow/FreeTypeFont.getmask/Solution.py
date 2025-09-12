from PIL import Image, ImageDraw, ImageFont

# Function to create a bitmap for the given text
def create_text_bitmap(text, font_size=20, image_size=(200, 100), bg_color=(255, 255, 255), text_color=(0, 0, 0)):
    # Create an image with the specified background color
    image = Image.new("RGB", image_size, bg_color)
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.truetype("arial.ttf", font_size)
    
    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (image_size[0] - text_width) / 2
    text_y = (image_size[1] - text_height) / 2
    
    # Draw the text on the image
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    
    return image

# Example usage
bitmap = create_text_bitmap("Hello, World!", font_size=30)
bitmap.show()
