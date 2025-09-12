import scipy.ndimage

def calculate_median_filter(image, size):
    return scipy.ndimage.median_filter(image, size=size)

# Example usage:
image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filtered_image = calculate_median_filter(image, size=3)
print(filtered_image)
