
from PIL import Image, Draw

# Create a new image with the dimensions (500, 500)
image = Image.new('RGB', (500, 500), (255, 255, 255))

# Create a drawing object to draw on the image
draw = Draw(image)

# Set the line width and color
draw.line_width = 5
draw.fillcolor = (100, 200, 100)

# Draw a red line from (0, 0) to (400, 400)
draw.line((0, 0), (400, 400))

# Draw a green line from (400, 400) to (0, 400)
draw.line((400, 400), (0, 400))

# Save the image as "output.png"
image.save("output.png")
