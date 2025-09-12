from PIL import Image, ImageDraw

# Create a new image with a background color
image = Image.new('RGBA', (100, 100), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Define the parameters of the rounded rectangle
top_left = (20, 20)
bottom_right = (80, 80)
fill_color = 'blue'
outline_color = 'red'
radius = 10

# Draw the rounded rectangle
draw.rounded_rectangle([top_left, bottom_right], radius, fill=fill_color, outline=outline_color)

# Show the image
image.show()
