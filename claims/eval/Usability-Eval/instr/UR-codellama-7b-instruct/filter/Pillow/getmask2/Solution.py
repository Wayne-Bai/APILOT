
from PIL import Image, ImageDraw, ImageFont

# Set the text and font options
text = "Hello World!"
font_path = "/path/to/font.ttf"
font_size = 32
font_color = (0, 0, 0)

# Create a new image with a transparent background
image = Image.new("RGBA", (1024, 1024), (255, 255, 255, 0))

# Draw the text on the image using the selected font and color
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, font_size)
text_width, text_height = draw.text_size(text, font=font)
draw.text((0, 0), text, fill=font_color, font=font)

# Save the image to a file
image.save("my_bitmap_image.png")
