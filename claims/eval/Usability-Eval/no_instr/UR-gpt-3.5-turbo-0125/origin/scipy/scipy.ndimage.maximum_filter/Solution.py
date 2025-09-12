
import numpy as np
from scipy.ndimage import maximum_filter

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filter_size = 3

result = maximum_filter(data, size=filter_size)
print(result)
