import numpy as np
from scipy.ndimage import gaussian_filter

# Example usage:
# Create a sample 2D array (image)
image = np.random.rand(100, 100)

# Apply a Gaussian filter with a standard deviation of 2.0
filtered_image = gaussian_filter(image, sigma=2.0)

# Display the original and filtered images (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Filtered Image')
plt.imshow(filtered_image, cmap='gray')

plt.show()
