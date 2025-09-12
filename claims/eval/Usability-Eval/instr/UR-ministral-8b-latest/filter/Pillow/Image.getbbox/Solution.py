from PIL import Image

def calculate_bounding_box(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        grayscale_img = img.convert('L')

        # Get the array of pixels
        pixels = grayscale_img.load()

        # Find the smallest x and y coordinates that have non-zero pixels
        min_x = min_y = None
        max_x = max_y = 0

        for y in range(grayscale_img.height):
            for x in range(grayscale_img.width):
                if pixels[x, y] > 0:  # Check for non-zero pixels
                    if min_x is None or x < min_x:
                        min_x = x
                    if min_y is None or y < min_y:
                        min_y = y
                    if max_x < x:
                        max_x = x
                    if max_y < y:
                        max_y = y

        # Return the bounding box as (min_x, min_y, max_x, max_y)
        return (min_x, min_y, max_x, max_y)

# Example usage
bbox = calculate_bounding_box('path_to_image.jpg')
print(bbox)
