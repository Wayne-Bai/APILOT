from PIL import Image, ImageDraw, ImageFont

# Initialize the text graphic
text = "Hello, World!"
draw = ImageDraw.Draw(Image.new("RGB", (500, 100)))

# Choose a font and size
font = ImageFont.truetype("arial.ttf", 50)

# Draw the text on the image
draw.text((25, 50), text, fill=(0, 0, 0), font=font)

# Save the image
draw.image.save("text_bitmap.png")
