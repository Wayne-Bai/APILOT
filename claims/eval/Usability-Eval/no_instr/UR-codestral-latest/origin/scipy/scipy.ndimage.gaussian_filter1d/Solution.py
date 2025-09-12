import numpy as np
from scipy import ndimage

# create an example input array
x = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0])

# apply a 1-D Gaussian filter with sigma=1
y = ndimage.gaussian_filter1d(x, sigma=1)

print(y)
