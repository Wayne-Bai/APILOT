from PIL import Image, ImageDraw, ImageFont

def create_bitmap_with_text(text, font_path='arial.ttf', font_size=24):
    # Create a font object
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate text size to create an appropriate image size
    text_width, text_height = font.getsize(text)
    
    # Create an image with a white background
    image = Image.new('RGB', (text_width, text_height), 'white')
    
    # Create a draw object
    draw = ImageDraw.Draw(image)
    
    # Draw the text onto the image
    draw.text((0, 0), text, font=font, fill='black')
    
    return image

# Example usage
bitmap = create_bitmap_with_text('Hello, World!')
bitmap.show()
