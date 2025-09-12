import numpy as np
from scipy import signal

# Example function to apply a 3x3 maximum filter
def apply_max_filter(image, window_shape):
    kernel_size = window_shape
    high_pass = np.zeros(image.shape, dtype=np.float32)

    image_flatten = image.flatten()
    height, width = image.shape

    for j in range(height):
        for i in range(width):
            start, stop = i - kernel_size[0]//2, i + kernel_size[0]//2
            start = max(0, start)
            stop = min(width, stop)

            for ii in range(start, stop):
                start_j, stop_j = j - kernel_size[1]//2, j + kernel_size[1]//2
                start_j = max(0, start_j)
                stop_j = min(height, stop_j)

                crop = image_flatten[start_j * width + ii:stop_j * width + ii]
                high_pass[j, i] = np.max(crop)

    return high_pass

# Define a sample 2D image
image = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# Define the size of the window
window_size = (3, 3)

# Apply the maximum filter
filtered_image = apply_max_filter(image, window_size)
print(filtered_image)
