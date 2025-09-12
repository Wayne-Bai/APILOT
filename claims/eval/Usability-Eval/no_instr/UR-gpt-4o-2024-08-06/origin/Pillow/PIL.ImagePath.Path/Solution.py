from PIL import Image, ImageDraw

# Create a new image with white background
width, height = 400, 400
image = Image.new("RGB", (width, height), "white")

# Prepare the drawing context
draw = ImageDraw.Draw(image)

# Draw a red rectangle
draw.rectangle(((50, 50), (350, 350)), outline="red", width=5)

# Draw a blue line
draw.line((50, 350, 350, 50), fill="blue", width=3)

# Draw a green circle
draw.ellipse((150, 150, 250, 250), outline="green", width=3)

# Save the image
image.save("vector_image.png")

# Optionally, show the image if you have a GUI environment
# image.show()
