# Import the required library
from PIL import Image, ImageDraw, ImageFont

# Specify the text you want to create a bitmap for
text = "Hello, World!"

# Specify the font you want to use
font = ImageFont.truetype("arial.ttf", 36)  # You can change the font and size as per your requirement

# Create an image with white background and the size of the image will be determined by the text
image_width = font.getsize(text)[0] + 20  # Add some padding
image_height = font.getsize(text)[1] + 20  # Add some padding

img = Image.new("RGB", (image_width, image_height), (255, 255, 255))

# Create a drawing context and draw the text onto the image
d = ImageDraw.Draw(img)

# Specify the position and the color of the text
x, y = 10, 10
d.text((x, y), text, fill=(0, 0, 0), font=font)

# Save the image to a file
img.save("text_bitmap.png")
