import scipy
import numpy as np
from scipy.ndimage import filters, measurements

# Input array
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).astype(float)

# Percentile to be calculated
percentile = 50

# Compute the percentile filter
percentile_filter = filters.percentile_filter(x, percentile, size=(2,2))

print(percentile_filter)
