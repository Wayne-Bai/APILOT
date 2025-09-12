from PIL import Image

def calculate_bounding_box(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Convert the image to grayscale
    img = img.convert('L')
    # Get the image data as a numpy array
    data = np.array(img)
    # Find the indices of the non-zero regions
    non_zero_indices = np.nonzero(data)
    # Calculate the bounding box
    x_min, x_max = non_zero_indices[1].min(), non_zero_indices[1].max()
    y_min, y_max = non_zero_indices[0].min(), non_zero_indices[0].max()
    # Return the bounding box
    return (x_min, x_max, y_min, y_max)
