
from PIL import Image

# Load the image
image = Image.open("image.jpg")

# Convert the image to grayscale
gray_image = image.convert("L")

# Apply a threshold to the image to binarize it
threshold = 128
binary_image = gray_image.point(lambda x: 0 if x <= threshold else 255)

# Find the bounding box of the non-zero regions in the image
bounding_boxes = []
for i in range(binary_image.width):
    for j in range(binary_image.height):
        pixel = binary_image.getpixel((i, j))
        if pixel > 0:
            bounding_boxes.append((i, j))

# Calculate the bounding box of the non-zero regions
x1 = min(bounding_boxes, key=lambda x: x[0])[0]
y1 = min(bounding_boxes, key=lambda x: x[1])[1]
x2 = max(bounding_boxes, key=lambda x: x[0])[0]
y2 = max(bounding_boxes, key=lambda x: x[1])[1]

print("Bounding box of the non-zero regions in the image:")
print("  (x1, y1): ({}, {})".format(x1, y1))
print("  (x2, y2): ({}, {})".format(x2, y2))
