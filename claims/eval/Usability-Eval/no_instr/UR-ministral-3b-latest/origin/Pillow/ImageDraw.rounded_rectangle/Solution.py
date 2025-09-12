from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
img = Image.new("RGB", (200, 200), "white")

# Create an ImageDraw object
draw = ImageDraw.Draw(img)

# Specify the rectangle coordinates and rounded corners radius
rect = (20, 20, 180, 180)
radius = 10

# Draw a rounded rectangle
draw.ellipse([(x - radius, y - radius, -(x - 20) + radius, y - radius + radius)]*2, outline="black")
draw.rectangle(rect, outline="black")

# Save or display the image (uncomment the following line to display it)
# img.show()

# Alternatively, you can save the image to a file
img.save("rounded_rectangle.png")
