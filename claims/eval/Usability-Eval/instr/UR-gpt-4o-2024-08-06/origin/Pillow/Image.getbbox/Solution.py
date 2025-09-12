from PIL import Image

def calculate_bounding_box(image_path):
    with Image.open(image_path) as image:
        # Convert image to binary (black and white) if it's not already
        image = image.convert('L').point(lambda x: 0 if x == 0 else 1, '1')
        
        # Load pixel data
        pixels = image.load()
        
        # Initialize bounding box values
        min_x, min_y = image.width, image.height
        max_x, max_y = 0, 0

        # Iterate through each pixel to find non-zero regions
        for y in range(image.height):
            for x in range(image.width):
                if pixels[x, y] != 0:  # A non-zero pixel
                    if x < min_x:
                        min_x = x
                    if y < min_y:
                        min_y = y
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y

        # Return bounding box as a tuple (left, upper, right, lower)
        if min_x <= max_x and min_y <= max_y:
            return (min_x, min_y, max_x + 1, max_y + 1)
        else:
            return None

# Example usage:
# bounding_box = calculate_bounding_box('path_to_image.png')
# print(bounding_box)
