import scipy.ndimage as ndimage
from scipy.stats import rankdata

def multidimensional_rank_filter(image, size, percentile):
    """
    Calculate a multidimensional rank filter.

    Parameters:
    - image: 2D image array to filter
    - size: tuple specifying the size of the window (e.g., (3, 3) for a 3x3 window)
    - percentile: float between 0 and 100

    Returns:
    - filtered_image: 2D image array with the rank filter applied
    """
    # Calculate rank data
    ranked_image = rankdata(image, method='auto')

    # Define the output variable
    filtered_image = ndimage.uniform_filter(ranked_image, size=size, mode='constant')

    # Apply the percentile filter
    filtered_image排名 = filtered_image * (percentile / 100)

    return filtered_image排名

# Example usage
image = [[2.1, 3.2, 4.5], [5.6, 6.7, 7.8], [8.9, 10.1, 11.2]]
size = (3, 3)
percentile = 90.0

filtered_image = multidimensional_rank_filter(image, size, percentile)
print(filtered_image)
