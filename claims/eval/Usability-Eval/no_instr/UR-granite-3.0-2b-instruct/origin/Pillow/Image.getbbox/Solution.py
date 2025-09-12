from PIL import Image

def calculate_bounding_box(image_path):
    image = Image.open(image_path)
    width, height = image.size

    # Find non-zero pixels
    non_zero_pixels = image.getdata()
    non_zero_pixels = [pixel for pixel in non_zero_pixels if pixel != 0]

    # Calculate bounding box
    x_min, x_max = min(non_zero_pixels, key=lambda x: (x[0], -x[1])), max(non_zero_pixels, key=lambda x: (x[0], -x[1]))
    y_min, y_max = min(non_zero_pixels, key=lambda y: (y[1], -y[0])), max(non_zero_pixels, key=lambda y: (y[1], -y[0]))

    return (x_min, y_min, x_max, y_max)

# Example usage
image_path = "path/to/your/image.png"
bounding_box = calculate_bounding_box(image_path)
print(f"Bounding box: {bounding_box}")
