from PIL import Image, ImageDraw, ImageFont

# Define the text to be rendered
text = "Hello, World!"

# Define the font and size
font = ImageFont.truetype("arial.ttf", 40)

# Calculate the size required to fit the text
text_width, text_height = font.getsize_multiline(text)

# Create a new image with white background
image = Image.new('RGB', (text_width, text_height), color='white')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Draw the text onto the image
draw.text((0, 0), text, font=font, fill='black')

# Save the image
image.save("text_bitmap.png")
