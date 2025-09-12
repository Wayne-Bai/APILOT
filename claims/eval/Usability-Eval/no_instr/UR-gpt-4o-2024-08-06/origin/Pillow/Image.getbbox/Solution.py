from PIL import Image

def calculate_bounding_box(image_path):
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        gray_image = img.convert("L")
        
        # Get image data
        image_data = gray_image.getdata()

        # Initialize min/max coordinates
        min_x, min_y, max_x, max_y = img.width, img.height, 0, 0

        # Loop through each pixel in the image
        for y in range(img.height):
            for x in range(img.width):
                pixel_value = image_data[y * img.width + x]
                
                # If the pixel is not zero, update bounding box coordinates
                if pixel_value != 0:
                    if x < min_x:
                        min_x = x
                    if y < min_y:
                        min_y = y
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y

        # Check if any non-zero region was detected
        if min_x > max_x or min_y > max_y:
            return None  # No non-zero regions found

        # Return the bounding box as a tuple (left, upper, right, lower)
        return (min_x, min_y, max_x, max_y)

# Example usage:
# bounding_box = calculate_bounding_box("example_image.png")
# print(bounding_box)
