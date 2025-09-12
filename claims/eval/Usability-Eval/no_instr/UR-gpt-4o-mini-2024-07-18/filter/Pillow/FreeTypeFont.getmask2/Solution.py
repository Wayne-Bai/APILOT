from PIL import Image, ImageDraw, ImageFont

def create_bitmap_with_text(text, font_path, font_size, image_size):
    # Create a new image with white background
    image = Image.new('RGB', image_size, 'white')
    draw = ImageDraw.Draw(image)
    
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate text size and position
    text_size = draw.textsize(text, font=font)
    text_x = (image_size[0] - text_size[0]) // 2
    text_y = (image_size[1] - text_size[1]) // 2
    
    # Draw the text
    draw.text((text_x, text_y), text, font=font, fill='black')
    
    return image

# Example usage
bitmap = create_bitmap_with_text("Hello, World!", "path/to/font.ttf", 40, (400, 200))
bitmap.show()
