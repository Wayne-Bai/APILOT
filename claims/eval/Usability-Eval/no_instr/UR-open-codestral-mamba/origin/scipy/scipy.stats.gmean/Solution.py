import scipy.stats as stats

def weighted_geometric_mean(a, weights, axis=None):
    return stats.gmean(a, axis)

# test the function
a = [1, 2, 3, 4, 5]
weights = [1, 1, 1, 1, 1]
print("Weighted Geometric Mean: ", weighted_geometric_mean(a, weights))
