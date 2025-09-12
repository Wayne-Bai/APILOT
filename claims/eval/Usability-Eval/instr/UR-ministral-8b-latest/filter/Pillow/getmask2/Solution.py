from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background and set the size
image = Image.new('RGB', (400, 200), color = 'white')
d = ImageDraw.Draw(image)

# Load a TrueType font
font = ImageFont.truetype('arial.ttf', 36)

# Define the text to embed
text = "Hello, Pillow!"

# Define the position where the text will be placed
position = (50, 100)

# Add the text to the image
image = d.text((position[0], position[1]), text, fill="black", font=font)

# Save the image
image.save('output_image.png')

# Display the image (uncomment the line below to see the image in your local system/terminal)
image.show()
