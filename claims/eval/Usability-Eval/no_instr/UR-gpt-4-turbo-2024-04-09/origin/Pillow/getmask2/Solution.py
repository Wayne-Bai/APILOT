from PIL import Image, ImageDraw, ImageFont

def create_text_bitmap(text, font_path, font_size, output_path):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Create a new image with white background
    image_size = (500, 200)
    image = Image.new("RGB", image_size, "white")
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Calculate text width and height
    text_width, text_height = draw.textsize(text, font=font)
    
    # Calculate position
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2
    
    # Draw the text on image
    draw.text((x, y), text, font=font, fill="black")
    
    # Save the image
    image.save(output_path)

# Example usage
text = "Hello, World!"
font_path = "arial.ttf"  # Path to a .ttf font file on your system
font_size = 24
output_file = "text_image.png"
create_text_bitmap(text, font_path, font_size, output_file)
