
from PIL import Image, ImageDraw
# Create a new image
img = Image.new('RGB', (200, 100), color='white')
# Create a drawing object
draw = ImageDraw.Draw(img)
# Define the coordinates and radius of the rounded rectangle
x1, y1, x2, y2 = 20, 20, 180, 80
radius = 20
# Draw the rounded rectangle
draw.roundrect((x1, y1, x2, y2), radius, fill='black')
# Save the image
img.save('rounded_rectangle.png')
