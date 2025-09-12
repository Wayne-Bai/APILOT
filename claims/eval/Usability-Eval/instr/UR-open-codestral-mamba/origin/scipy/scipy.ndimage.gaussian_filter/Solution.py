import scipy.ndimage as ndimage
from scipy import misc
import matplotlib.pyplot as plt

# Load the image
image = misc.face(gray=True)

# Execute the 2D Gaussian filter
blurred_image = ndimage.gaussian_filter(image, sigma=5)

# Display the original and blurred images
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].imshow(image, cmap='gray')
ax[0].axis('off')
ax[0].set_title('Original Image')

ax[1].imshow(blurred_image, cmap='gray')
ax[1].axis('off')
ax[1].set_title('Blurred (Gaussian filtered) Image')

plt.show()
