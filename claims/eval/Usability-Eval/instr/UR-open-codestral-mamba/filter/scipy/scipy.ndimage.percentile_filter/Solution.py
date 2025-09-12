import scipy.ndimage
import numpy as np

# creating a 3-D test array
size = 5, 6, 8
a = np.random.rand(*size)

# calculating the 20th percentile filter
percentile_filter = scipy.ndimage.percentile_filter(a, 20, size=(2,2,2))

print(percentile_filter)
