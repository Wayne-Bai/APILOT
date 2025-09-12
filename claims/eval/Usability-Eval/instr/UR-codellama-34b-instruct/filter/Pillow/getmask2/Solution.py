from PIL import Image, ImageFont, ImageDraw

# Define the font size and color
font_size = 24
font_color = (0, 0, 0) # black

# Create a new image with a transparent background
img = Image.new('RGBA', (512, 512), (255, 255, 255)) # create a 512x512 image with a white background

# Load the font
font = ImageFont.truetype("arial.ttf", font_size)

# Draw the text on the image
draw = ImageDraw.Draw(img)
text_width, text_height = draw.textsize("Hello, World!", font=font)
x = (512 - text_width)/2
y = (512 - text_height)/2
draw.text((x, y), "Hello, World!", font=font, fill=font_color)

# Save the image to a file
img.save("hello_world.png")
