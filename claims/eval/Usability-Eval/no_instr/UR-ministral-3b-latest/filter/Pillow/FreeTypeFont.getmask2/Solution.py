from PIL import Image, ImageDraw, ImageFont

# Create a new image (white background)
image = Image.new('RGB', (800, 400), 'white')

# Create a drawing context on the image
draw = ImageDraw.Draw(image)

# Load a font file (VGA8 441 font as an example)
font = ImageFont.truetype('path/to/your/font.ttf', size=36)

# Define the text and position
text = "Hello, World!"
position = (100, 200)

# Draw the text on the image
draw.text(position, text, font=font, fill='black')

# Save the image
image.save('output_with_text.png')

# Show the image
image.show()
