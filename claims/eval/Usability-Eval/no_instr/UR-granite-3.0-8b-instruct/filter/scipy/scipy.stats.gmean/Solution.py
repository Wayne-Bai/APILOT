from scipy.stats import gmean

# Assuming 'data' is your 2D array and 'axis' is the axis along which you want to compute the weighted geometric mean
# 'weights' is the array of weights for each element in 'data'

weighted_geometric_mean = gmean(data, axis=axis, weights=weights)
