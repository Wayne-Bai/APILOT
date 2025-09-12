
import numpy as np
from scipy.ndimage import filters

# Define the kernel size for the median filter
kernel_size = (3, 3)

# Define the input image
img = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply the median filter to the input image
median_filtered_img = filters.median_filter(img, kernel_size)

# Print the output image
print(median_filtered_img)
