from scipy import ndimage

# Assuming 'image' is your input 2D array and 'size' is the size of the filter
image = ndarray  # Replace with your actual image
size = 3  # Replace with the desired filter size

# Implementing a simple uniform filter (mean filter)
filtered_image = ndimage.uniform_filter(image, size=size)

print(filtered_image)
