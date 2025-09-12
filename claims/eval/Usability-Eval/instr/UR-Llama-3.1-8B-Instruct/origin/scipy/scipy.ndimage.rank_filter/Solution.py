import numpy as np
from scipy import spatial
from scipy import ndimage

# Define a function to calculate the multidimensional rank filter
def multidimensional_rank_filter(image, rank, mode):
    """
    This function applies a multidimensional rank filter to the given image.

    Parameters:
    image (numpy array): The input image to be filtered.
    rank (int): The rank of the filter.
    mode (str): The mode of the filter. Options are 'nearest','mean', 'bilinear', 'bicubic','sinc', 'lanczos'.

    Returns:
    filtered_image (numpy array): The filtered image.
    """

    # Apply the rank filter using the ndimage.rank_filter function
    filtered_image = ndimage.rank_filter(image, rank, size=None, mode=mode)

    return filtered_image

# Create a sample 2D image
image = np.random.rand(10, 10)

# Apply the rank filter with a rank of 10 and 'nearest' mode
filtered_image = multidimensional_rank_filter(image, 10, 'nearest')

# Print the original and filtered images
print('Original Image:')
print(image)
print('\nFiltered Image:')
print(filtered_image)
