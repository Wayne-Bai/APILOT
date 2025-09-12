
from PIL import Image

def calculate_bounding_box(image_path):
    image = Image.open(image_path)
    image_data = image.load()

    width, height = image.size
    min_x = width - 1
    min_y = height - 1
    max_x = 0
    max_y = 0

    for x in range(width):
        for y in range(height):
            if image_data[x, y] != 0:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    bounding_box = (min_x, min_y, max_x, max_y)
    return bounding_box

# Example usage
image_path = "image.jpg"
bounding_box = calculate_bounding_box(image_path)
print("Bounding box coordinates:", bounding_box)
