from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 500, 500
image = Image.new('RGB', (width, height), 'white')

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define a set of 2D vectors
vectors = [
    (100, 100), (200, 150), (250, 100),
    (350, 200), (400, 250), (450, 300)
]

# Plot the vector data
for (x, y) in vectors:
    draw.ellipse([(x-5, y-5), (x+5, y+5)], fill='blue')

# Display the image
image.show()

# Save the image to a file
image.save('vectors_image.png')
