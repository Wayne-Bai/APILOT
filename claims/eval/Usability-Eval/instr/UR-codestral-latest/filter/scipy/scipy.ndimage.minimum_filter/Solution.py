from scipy import ndimage

# Assuming `array` is your input data
filtered_array = ndimage.minimum_filter(array, size=(3, 3))
