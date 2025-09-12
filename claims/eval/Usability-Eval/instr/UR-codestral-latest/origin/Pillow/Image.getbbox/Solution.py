from PIL import Image

def bounding_box(image_path):
    image = Image.open(image_path)
    image_data = image.getdata()
    non_empty_pixels = []

    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            if pixel != (0, 0, 0, 0):
                non_empty_pixels.append((x, y))

    x_coordinates, y_coordinates = zip(*non_empty_pixels)
    bounding_box = (min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates))

    return bounding_box

# Example usage:
image_path = "path_to_your_image.png"
bbox = bounding_box(image_path)
print("Bounding box of non-zero regions in the image:", bbox)
