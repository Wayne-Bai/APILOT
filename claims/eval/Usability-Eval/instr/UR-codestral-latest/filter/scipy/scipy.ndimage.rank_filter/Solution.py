import scipy.stats as stats
import numpy as np

# Input data
data = np.array([[9, 2, 5], [4, 7, 1], [6, 3, 8]])

# Calculate rank for each element in the array
ranked_data = stats.rankdata(data, method='average')

# Reshape the rank data to match original data shape
multidimensional_rank = ranked_data.reshape(data.shape)

print("Original data:\n", data)
print("\nMultidimensional rank:\n", multidimensional_rank)
