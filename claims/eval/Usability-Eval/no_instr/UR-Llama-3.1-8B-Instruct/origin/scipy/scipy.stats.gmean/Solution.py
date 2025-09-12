from scipy import stats

# Define a sample 2D array
array_2d = [[1, 2, 3], [4, 5, 6]]

# Define the weights for each element
weights = [0.5, 0.3, 0.2]

# Compute the weighted geometric mean along the 0th axis (i.e., rows)
weighted_geometric_mean_rows = stats.weightedmean(np.array(array_2d), np.array(weights), axis=0)

# Compute the weighted geometric mean along the 1st axis (i.e., columns)
weighted_geometric_mean_cols = stats.weightedmean(np.array(array_2d), np.array(weights), axis=1)
