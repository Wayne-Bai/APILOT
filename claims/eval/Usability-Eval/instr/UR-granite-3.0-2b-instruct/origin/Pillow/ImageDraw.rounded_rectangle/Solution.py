from PIL import Image, ImageDraw

# Create a new image with a white background
img = Image.new('RGB', (200, 200), color = (255, 255, 255))

# Create a drawing object
d = ImageDraw.Draw(img)

# Draw a rounded rectangle
d.rectangle((50, 50, 150, 150), outline = (0, 0, 0), width = 5)

# Save the image
img.save('rounded_rectangle.png')
