import numpy as np
from scipy.ndimage import minimum_filter

# Assuming you have a NumPy array `data`
filtered_data = minimum_filter(data, size=3)
