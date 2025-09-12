from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define some 2D vector data points
points = [(100, 100), (300, 100), (300, 300), (100, 300)]

# Draw the vector data as a polygon
draw.polygon(points, outline="black", fill="lightblue")

# Save the image
image.save("vector_data.png")

# Optionally, display the image
image.show()
