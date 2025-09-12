from PIL import Image

# Load the image
image_path = 'example.jpg'
image = Image.open(image_path)

# Convert the image to grayscale
image_gray = image.convert('L')

# Calculate the bounding box of the non-zero regions
image_gray_data = image_gray.getdata()
max_width, max_height = image.size

bounding_box = None
for y in range(max_height):
    for x in range(max_width):
        if image_gray_data[y * max_width + x] != 0:
            if bounding_box is None:
                bounding_box = (x, y, x, y)
            elif bounding_box[0] > x:
                bounding_box = (x, bounding_box[1], x, bounding_box[3])
            elif bounding_box[2] < y:
                bounding_box = (bounding_box[0], y, bounding_box[2], y)
            elif bounding_box[1] < y:
                bounding_box[1] = y
            elif bounding_box[1] > y:
                bounding_box[1] = y
            elif bounding_box[3] < x:
                bounding_box = (bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3])
            elif bounding_box[3] > x:
                bounding_box = (bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3])

print(f"Bounding box coordinates: {bounding_box}")
