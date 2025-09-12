from PIL import Image, ImageDraw, ImageFont

def create_bitmap(text, font_path, font_size, bitmap_size):
    # Create a new blank image with a white background
    image = Image.new('RGB', bitmap_size, 'white')
    
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate text size
    text_width, text_height = draw.textsize(text, font)
    
    # Calculate position to center the text
    x = (bitmap_size[0] - text_width) / 2
    y = (bitmap_size[1] - text_height) / 2
    
    # Draw the text on the image
    draw.text((x, y), text, fill='black', font=font)
    
    return image

# Example usage
bitmap_image = create_bitmap("Hello, World!", "arial.ttf", 40, (400, 200))
bitmap_image.save("text_bitmap.png")
