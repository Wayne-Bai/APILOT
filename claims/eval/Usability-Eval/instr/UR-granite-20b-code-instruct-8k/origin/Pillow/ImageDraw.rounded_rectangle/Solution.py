from PIL import Image, ImageDraw

# Create a blank canvas with a size of 400x400 pixels
canvas = Image.new('RGB', (400, 400))

# Get a drawing context
draw = ImageDraw.Draw(canvas)

# Draw a rounded rectangle with a radius of 20 pixels
draw.rectangle([10, 10, 390, 390], fill=(255, 255, 255), outline=(0, 0, 0), width=2, radius=20)

# Save the image
canvas.save('rounded_rectangle.png')
