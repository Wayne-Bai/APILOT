import numpy as np

# Assuming arr is your two-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the 25th percentile
percentile_25 = np.percentile(arr, 25)

# Filter the array to keep only values above the 25th percentile
filtered_arr = np.where(arr > percentile_25, arr, np.nan)

print(filtered_arr)
