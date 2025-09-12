from PIL import Image, ImageCms

# Open the image file
img = Image.open('image.jpg')

# Create a color palette
palette = [
    (0, 0, 0),  # Black
    (255, 255, 255),  # White
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
]

# Convert the image to the new color palette
img_new_palette = img.convert('P', palette=palette, colors=len(palette))

# Save the new image
img_new_palette.save('image_new_palette.png')
