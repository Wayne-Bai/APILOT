from PIL import Image, ImageDraw, ImageFont

def create_bitmap_for_text(text, font_name, font_size, output_file):
    # Set font
    font = ImageFont.truetype(font_name, font_size)
    
    # Calculate the width and height of the text
    width, height = font.getsize(text)
    
    # Create a new image with white background and text size
    img = Image.new('RGB', (width + 10, height + 10), color = (73, 109, 137))
    
    # Set drawing context
    d = ImageDraw.Draw(img)
    
    # Draw text on the image
    d.text((5, 5), text, fill=(255,255,255), font=font)
    
    # Save the image to the specified output file
    img.save(output_file)

# Example usage:
create_bitmap_for_text('Hello, World!', 'arial.ttf', 20, 'hello_world.bmp')
