from PIL import Image, ImageDraw

# Create a new image with a white background
img = Image.new('RGB', (200, 200), color = (255, 255, 255))

# Create a drawing context
draw = ImageDraw.Draw(img)

# Draw a rounded rectangle
draw.rounded_rectangle([(10, 10), (180, 180)], radius=20, outline=(0, 0, 0), width=5)

# Save the image
img.save('rounded_rectangle.png')
