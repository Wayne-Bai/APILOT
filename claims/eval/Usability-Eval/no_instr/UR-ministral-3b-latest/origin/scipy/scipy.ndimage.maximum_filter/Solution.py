import scipy.ndimage as ndimage

# Example usage
input_image = ndimage.imread('image.png')  # path to your image file
filtered_image = ndimage.filters.median_filter(input_image, size=(5, 5))  # replace with the desired filter size
ndimage.zoom(filtered_image, zoom=(1, 1, 1, 1), order=1)

