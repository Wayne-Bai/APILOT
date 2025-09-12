from PIL import Image

# Create a new image with a white background
img = Image.new('RGB', (100, 100), color = (255, 255, 255))

# Create a new image with a black background
img2 = Image.new('RGB', (100, 100), color = (0, 0, 0))

# Paste the first image onto the second image at a specific position
img2.paste(img, (50, 50), img)

# Save the resulting image to a file
img2.save('result.png')
