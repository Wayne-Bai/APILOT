import numpy as np
from scipy.ndimage import rank_filter

def apply_rank_filter(image, size, rank):
    """
    Apply a multidimensional rank filter to an image.

    Args:
    - image: ndarray, input image
    - size: int or tuple, size of the filter
    - rank: int, rank of the filter

    Returns:
    - filtered_image: ndarray, output filtered image
    """
    filtered_image = rank_filter(image, rank, size=size)
    return filtered_image

# Example usage:
if __name__ == "__main__":
    # Create a sample 2D image (numpy array)
    sample_image = np.random.random((10, 10))
    
    # Apply the rank filter
    size = 3  # Filter size
    rank = 1  # Rank
    result = apply_rank_filter(sample_image, size, rank)
    
    print("Original Image:\n", sample_image)
    print("Filtered Image:\n", result)
