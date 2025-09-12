from PIL import Image, ImageDraw, ImageFont

# Function to create a bitmap for the given text
def create_text_bitmap(text, font_path='arial.ttf', font_size=40, output_file='text_bitmap.png'):
    # Create a font object
    font = ImageFont.truetype(font_path, font_size)
    
    # Determine the size required for the image
    width, height = font.getsize(text)
    
    # Create a new image with a white background
    image = Image.new('RGB', (width, height), 'white')
    
    # Create a Draw object
    draw = ImageDraw.Draw(image)
    
    # Draw the text on the image
    draw.text((0, 0), text, font=font, fill='black')
    
    # Save the image to a file
    image.save(output_file)

# Example usage
create_text_bitmap("Hello, World!")
