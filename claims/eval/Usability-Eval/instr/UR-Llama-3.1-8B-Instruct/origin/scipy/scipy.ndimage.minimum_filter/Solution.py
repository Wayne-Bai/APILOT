import numpy as np
from scipy.ndimage import minimum_filter
import matplotlib.pyplot as plt

# Create a noisy image
image = np.random.rand(10, 10)

# Perform minimum filter with a radius of 2
filtered_image = minimum_filter(image, size=(3, 3))

# Display the original and filtered images
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.show()
