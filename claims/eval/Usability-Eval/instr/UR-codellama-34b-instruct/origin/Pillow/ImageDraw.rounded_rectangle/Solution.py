
from PIL import Image, ImageDraw

# Create a new image with a black background
image = Image.new('RGBA', (500, 500), (0, 0, 0))
draw = ImageDraw.Draw(image)

# Set the outline color and width
outline_color = (255, 255, 255)
outline_width = 10

# Draw a rounded rectangle using draw_round_rectangle() function
draw.draw_round_rectangle(outline_color, outline_width)

# Save the image to disk
image.save('rounded_rectangle.png')
