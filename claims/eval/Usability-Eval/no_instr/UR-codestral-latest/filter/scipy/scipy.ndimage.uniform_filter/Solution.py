import numpy as np
from scipy import ndimage

data = np.random.random((100, 100))  # Replace this with your own data
filter_size = 3  # Define the size of the filter. Adjust as needed

result = ndimage.uniform_filter(data, size=filter_size)
