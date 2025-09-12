from PIL import Image, ImageDraw, ImageFont

def create_text_bitmap(text, font_path, font_size):
    # Load a font
    font = ImageFont.truetype(font_path, font_size)
    
    # Create image with transparent background
    image = Image.new("RGBA", (300, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Calculate text width and height
    text_width, text_height = draw.textsize(text, font=font)

    # Resize image based on text size
    image = image.resize((text_width, text_height))

    draw = ImageDraw.Draw(image)
    # Position the text
    text_position = (0, 0)
    
    # Draw the text
    draw.text(text_position, text, font=font, fill="black")

    image.show()

# Example usage
create_text_bitmap("Hello, World!", "arial.ttf", 24)
