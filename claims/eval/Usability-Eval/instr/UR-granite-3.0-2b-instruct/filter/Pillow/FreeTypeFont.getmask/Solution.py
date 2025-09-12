from PIL import Image, ImageDraw, ImageFont

# Set the text and font
text = "Hello, World!"
font = ImageFont.truetype("arial.ttf", 15)

# Create a new image with a white background
img = Image.new("RGB", (200, 50), color = (255, 255, 255))

# Create a drawing object
d = ImageDraw.Draw(img)

# Draw the text on the image
d.text((10, 10), text, font=font, fill=(0, 0, 0))

# Save the image
img.save("text_bitmap.png")
