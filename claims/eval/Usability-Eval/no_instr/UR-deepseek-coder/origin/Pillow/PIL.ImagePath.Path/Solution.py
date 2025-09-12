from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define some 2D vector data points
points = [(100, 100), (300, 150), (500, 100), (700, 150)]

# Draw lines connecting the points
draw.line(points, fill="blue", width=5)

# Draw circles at each point
for point in points:
    draw.ellipse((point[0]-10, point[1]-10, point[0]+10, point[1]+10), fill="red")

# Save the image
image.save("vector_data.png")

# Optionally, display the image
image.show()
