
import numpy as np
from scipy.signal import rank_order, rank_filter

# Define the input array
input_array = np.random.rand(10, 10)

# Calculate the ranks of the values in each dimension
ranks = rank_order(input_array)

# Apply the filter to the ranks
filtered_ranks = rank_filter(ranks, size=3)

# Convert the filtered ranks back to a 2D array
output_array = np.reshape(filtered_ranks, (10, 10))
