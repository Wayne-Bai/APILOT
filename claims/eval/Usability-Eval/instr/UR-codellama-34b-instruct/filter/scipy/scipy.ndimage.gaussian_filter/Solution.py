import numpy as np
from scipy.ndimage import gaussian_filter

# Load the image
img = np.array(Image.open('image.jpg'))

# Apply a Gaussian filter to the image with a standard deviation of 1
gauss_img = gaussian_filter(img, sigma=1)

# Display the filtered image
plt.imshow(gauss_img, cmap='gray')
