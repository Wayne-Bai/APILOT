import scipy.ndimage

def multidimensional_minimum_filter(image, size):
    # Perform multidimensional minimum filter on the image
    filtered_image = scipy.ndimage.minimum_filter(image, size)
    return filtered_image

# Usage Example
image = [[5, 2, 9, 4], [3, 7, 1, 8], [6, 4, 3, 0]]
size = 2

filtered_image = multidimensional_minimum_filter(image, size)
print(f"Filtered image:\n{filtered_image}")
