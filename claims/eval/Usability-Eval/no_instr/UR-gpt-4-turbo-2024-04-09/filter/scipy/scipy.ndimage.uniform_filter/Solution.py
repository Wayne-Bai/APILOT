import scipy.ndimage as ndimage
import numpy as np

# Example data: a multidimensional array
data = np.random.random((5, 5, 5))

# Applying a multidimensional uniform filter
filtered_data = ndimage.uniform_filter(data, size=3)
print(filtered_data)
