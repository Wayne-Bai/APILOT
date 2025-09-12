import numpy as np
from scipy.ndimage import gaussian_filter

def multidimensional_gaussian_filter(data, sigma, axes=0, order=3):
    # Apply Gaussian filter along the specified axes
    return gaussian_filter(data, sigma=sigma, axes=axes, order=order)

# Example usage:
data = np.random.rand(100, 100)  # 2D example data
filtered_data = multidimensional_gaussian_filter(data, sigma=1.0, axes=(0, 1))
print(filtered_data)
