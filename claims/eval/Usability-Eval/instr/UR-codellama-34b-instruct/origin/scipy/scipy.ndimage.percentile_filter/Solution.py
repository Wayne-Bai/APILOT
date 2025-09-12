import numpy as np
from scipy import stats

# Define the data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the percentile rank for each element in the data
rank_map = stats.percentile_rank(data, axis=0)

# Define the filter function
def filter_func(x):
    return np.all(rank_map >= x, axis=0)

# Apply the filter to the data
filtered_data = data[filter_func(2)]

print(filtered_data)
