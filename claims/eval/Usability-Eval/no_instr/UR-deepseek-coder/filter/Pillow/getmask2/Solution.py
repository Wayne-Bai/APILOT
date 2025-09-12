from PIL import Image, ImageDraw, ImageFont

# Define the text and font settings
text = "Hello, Pillow!"
font_size = 40
font_color = (0, 0, 0)  # Black color
background_color = (255, 255, 255)  # White color

# Load a font (you can specify the path to your font file)
font = ImageFont.truetype("arial.ttf", font_size)

# Calculate the size needed for the text
text_width, text_height = font.getsize(text)

# Create a new image with a white background
image = Image.new('RGB', (text_width, text_height), background_color)
draw = ImageDraw.Draw(image)

# Draw the text on the image
draw.text((0, 0), text, font=font, fill=font_color)

# Save the image
image.save("text_bitmap.png")
