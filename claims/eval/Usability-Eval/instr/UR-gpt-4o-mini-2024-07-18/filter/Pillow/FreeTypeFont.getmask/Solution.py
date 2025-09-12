from PIL import Image, ImageDraw, ImageFont

def create_bitmap_from_text(text, font_path, font_size, image_size):
    # Create a new image with white background
    image = Image.new('RGB', image_size, 'white')
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Load the specified font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (image_size[0] - text_width) // 2
    text_y = (image_size[1] - text_height) // 2
    
    # Draw the text on the image
    draw.text((text_x, text_y), text, fill='black', font=font)
    
    return image

# Example usage
bitmap_image = create_bitmap_from_text("Hello, World!", "arial.ttf", 32, (200, 100))
bitmap_image.show()
