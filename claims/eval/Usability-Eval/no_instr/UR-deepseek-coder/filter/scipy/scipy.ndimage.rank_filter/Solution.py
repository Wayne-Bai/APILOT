import numpy as np
from scipy.ndimage import rank_filter

# Example data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Define the rank and the size of the window (kernel)
rank = 1  # 1st smallest value in the window
window_size = (3, 3)  # 3x3 window

# Apply the rank filter
filtered_data = rank_filter(data, rank, size=window_size)

print(filtered_data)
