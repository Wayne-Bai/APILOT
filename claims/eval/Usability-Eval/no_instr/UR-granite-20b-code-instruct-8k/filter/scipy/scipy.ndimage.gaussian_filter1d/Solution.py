import numpy as np
from scipy.ndimage import gaussian_filter1d
# Assuming you have a 1-D array called 'data'
filtered_data = gaussian_filter1d(data, sigma=1)
