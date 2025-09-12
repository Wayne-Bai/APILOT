from scipy.stats import gmean

# Assuming you have a 2D array 'data'
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Compute the weighted geometric mean along the specified axis (0 in this case)
weighted_gmean = gmean(data, axis=0)

print(weighted_gmean)
