import scipy.stats as stats
def geometric_mean(data, weights):
    return stats.gmean(data, weights=weights, axis=0)

# Example usage:
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
weights = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
result = geometric_mean(data, weights)
print(result)
