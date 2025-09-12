from PIL import Image, ImageDraw, ImageFont

def create_text_bitmap(text, font_path, font_size, image_path):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate size of the required image
    dummy_image = Image.new("RGB", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy_image)
    text_width, text_height = dummy_draw.textsize(text, font=font)
    
    # Create an image with a white background
    image = Image.new("RGB", (text_width, text_height), "white")
    draw = ImageDraw.Draw(image)
    
    # Position the text at top left corner
    draw.text((0, 0), text, fill="black", font=font)
    
    # Save the image
    image.save(image_path)

# Example usage:
create_text_bitmap("Hello, World!", "arial.ttf", 24, "text_bitmap.png")
