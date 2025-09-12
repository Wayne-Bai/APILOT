import scipy.stats as stats

def calculate_relative_z_scores(data):
    return stats.zscore(data)

# Example usage
data = [10, 12, 14, 16, 18, 20]
z_scores = calculate_relative_z_scores(data)
print(z_scores)
