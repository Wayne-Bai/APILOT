import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the dimensions of the array
N = 10
M = 12

# Generate a random test image
image = np.random.rand(N, M)

# Calculate the median filter for the test image
median_filtered_image = signal.medfilt2d(image, kernel_size=(3, 3))

# Plot the original and filtered images
plt.figure()
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(median_filtered_image, cmap='gray')
plt.title('Median Filtered Image')
plt.show()
