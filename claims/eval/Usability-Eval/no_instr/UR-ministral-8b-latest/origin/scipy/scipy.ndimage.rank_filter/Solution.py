import numpy as np
import scipy.ndimage

def calculate_rank_filter(image, rank):
    # Create a filter array with 1 at the center and 0 on the edge
    filter_array = np.ones((rank, rank), dtype=bool)

    # Normalize the filter array
    filter_array = filter_array / np.sum(filter_array)

    # Apply the rank filter to the image
    filtered_image = scipy.ndimage.convolve(image, filter_array, mode='constant', cval=0.0)

    return filtered_image

# Example usage
image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank = 3

filtered_image = calculate_rank_filter(image, rank)
print("Filtered Image:")
print(filtered_image)
