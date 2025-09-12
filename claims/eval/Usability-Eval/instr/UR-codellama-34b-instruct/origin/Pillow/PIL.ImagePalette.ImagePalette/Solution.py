from PIL import Image

# Load the image and get its palette
image = Image.open("your_image.png")
palette = image.getpalette()

# Define the colors you want to use in the palette
colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255)   # Blue
]

# Create a new image with the same size as the original image
new_image = Image.new(image.mode, image.size, color=colors[0])

# Draw the original image on top of the new image
draw = ImageDraw.Draw(new_image)
draw.bitmap((0, 0), image, fill=(255, 255, 255))

# Save the new image
new_image.save("colorized_image.png")
