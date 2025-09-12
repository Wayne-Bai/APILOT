from PIL import Image, ImageDraw, ImageFont

def create_bitmap_with_text(text, font_size=20, image_size=(200, 100), background_color=(255, 255, 255), text_color=(0, 0, 0)):
    # Create a new image with the specified background color
    image = Image.new('RGB', image_size, background_color)
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.load_default()  # Using default font for simplicity
    
    # Calculate text size
    text_width, text_height = draw.textsize(text, font=font)
    
    # Calculate position for centered text
    text_x = (image_size[0] - text_width) // 2
    text_y = (image_size[1] - text_height) // 2
    
    # Draw the text on the image
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    
    return image

# Example usage
bitmap = create_bitmap_with_text("Hello, World!", font_size=24)
bitmap.show()
