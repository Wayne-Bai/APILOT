from PIL import Image

# Function to calculate non-zero region bounding box
def calculate_bounding_box(image):
    # Convert image to RGB if it is grayscale
    if len(image.getbands()) == 1:
        image = image.convert("RGB")

    # Threshold the image to create a binary image
    binary_image = Image.eval(image, lambda x: 1 if x != 0 else 0)

    # Find contours in the binary image
    from PIL import ImageOps
    binary_image = ImageOps.gray(binary_image)

    # Perform thresholding to get black and white image
    from scipy.ndimage import threshold_otsu
    threshold = threshold_otsu(binary_image)
    black_image = binary_image.point(lambda p: 0 if p < threshold else 1, alias=True)

    # Use contour to detect the overall shape
    import numpy as np
    img_array = np.array(black_image)
    contours, _ = cv2.findContours(img_array, mode=cv2.CHAIN_APPROX_SIMPLE, method=cv2.RETR_EXTERNAL)

    # Get the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the bounding box around the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    return (x, y, x+w, y+h)

# Example usage
if __name__ == "__main__":
    from PIL import Image

    img = Image.open("your_image_path_here")
    x, y, x2, y2 = calculate_bounding_box(img)
    print(f"Bounding Box Coordinates: ({x}, {y}, {x2}, {y2})")
