import numpy as np
from scipy.ndimage import filters

# Load the image data
image = np.array(Image.open('image_file.jpg'))

# Define the size of the uniform filter
filter_size = (3, 3)

# Apply the uniform filter to the image
uniform_filtered_image = filters.uniform_filter(image, size=filter_size)
