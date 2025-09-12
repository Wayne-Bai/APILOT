from PIL import Image
import numpy as np
# Open the image file
img = Image.open('example.jpg')
# Convert the image to a numpy array
arr = np.array(img)
# Calculate the bounding box of the non-zero regions
bbox = np.nonzero(arr)
# Print the bounding box
print(bbox)
