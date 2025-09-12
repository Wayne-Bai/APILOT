from scipy import ndimage

# Use ndimage.minimum_filter to calculate the multidimensional minimum filter
# Replace image with your actual image array and size with your desired filter size
filtered_image = ndimage.minimum_filter(image, size=3)
