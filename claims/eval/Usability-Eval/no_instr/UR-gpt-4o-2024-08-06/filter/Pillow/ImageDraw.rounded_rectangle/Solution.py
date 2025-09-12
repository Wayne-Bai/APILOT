from PIL import Image, ImageDraw

# Create an image with white background
width, height = 200, 200
image = Image.new('RGB', (width, height), 'white')

# Create a Draw object
draw = ImageDraw.Draw(image)

# Define rectangle properties
rectangle_position = (50, 50, 150, 150)
radius = 20

# Draw a rounded rectangle
draw.rounded_rectangle(rectangle_position, radius=radius, outline='black', width=2, fill='blue')

# Save or show the image
image.show()
# Or save the image to a file
# image.save('rounded_rectangle.png')
