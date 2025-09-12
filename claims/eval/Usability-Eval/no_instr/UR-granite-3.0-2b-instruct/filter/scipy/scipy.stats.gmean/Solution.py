from scipy.stats import gmean

# Assuming 'data' is your 2D array and 'weights' is your 1D array of weights
weighted_geometric_mean = gmean(data, axis=0, weights=weights)
