
import numpy as np
from scipy.ndimage import gaussian_filter

data = np.array([2, 4, 6, 8, 10])
sigma = 1.0

smoothed_data = gaussian_filter(data, sigma)

print(smoothed_data)
