import scipy.ndimage as nd
import numpy as np

# Define the 1D array (signal)
data = np.random.rand(100)

# Apply the 1D Gaussian filter
filtered_data = nd.gaussian_filter1d(data, sigma=2)
