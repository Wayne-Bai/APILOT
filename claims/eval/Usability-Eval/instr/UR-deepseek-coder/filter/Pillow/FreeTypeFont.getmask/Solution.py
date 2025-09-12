from PIL import Image, ImageDraw, ImageFont

def create_bitmap_text(text, font_path, font_size, text_color, bg_color, output_path):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate the size of the text
    text_width, text_height = font.getsize(text)
    
    # Create a new image with the calculated size
    image = Image.new('RGB', (text_width, text_height), bg_color)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Draw the text onto the image
    draw.text((0, 0), text, font=font, fill=text_color)
    
    # Save the image to the specified output path
    image.save(output_path)

# Example usage
text = "Hello, World!"
font_path = "arial.ttf"  # Path to your font file
font_size = 40
text_color = (255, 255, 255)  # White color
bg_color = (0, 0, 0)  # Black background
output_path = "output_text.png"

create_bitmap_text(text, font_path, font_size, text_color, bg_color, output_path)
