
from PIL import Image

# Load the image
image = Image.open("image.jpg")

# Convert the image to grayscale
gray = image.convert('L')

# Find all the non-zero pixels in the image
non_zero_pixels = []
for x in range(0, gray.size[0]):
    for y in range(0, gray.size[1]):
        if gray[x, y] != 0:
            non_zero_pixels.append((x, y))

# Calculate the bounding box of the non-zero pixels
min_x = min([pixel[0] for pixel in non_zero_pixels])
max_x = max([pixel[0] for pixel in non_zero_pixels])
min_y = min([pixel[1] for pixel in non_zero_pixels])
max_y = max([pixel[1] for pixel in non_zero_pixels])
bounding_box = (min_x, min_y, max_x, max_y)

# Print the bounding box
print("Bounding box:", bounding_box)
