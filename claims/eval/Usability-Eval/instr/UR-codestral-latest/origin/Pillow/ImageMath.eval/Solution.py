from PIL import Image, ImageDraw

# Create a new image with a white background
img = Image.new('RGB', (200, 200), color = (255, 255, 255))
d = ImageDraw.Draw(img)

# Draw a face (circle)
d.ellipse([(50, 50), (150, 150)], fill=(255, 255, 0))

# Draw eyes (small circles)
d.ellipse([(75, 75), (95, 95)], fill=(0, 0, 0))
d.ellipse([(105, 75), (125, 95)], fill=(0, 0, 0))

# Draw a smile (arc)
d.arc([(70, 100), (130, 150)], start=200, end=360, fill =(0, 0, 0))

# Display the image
img.show()
