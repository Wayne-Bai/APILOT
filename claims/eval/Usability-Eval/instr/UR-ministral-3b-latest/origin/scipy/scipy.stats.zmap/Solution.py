import scipy.stats as stats

# Example data
data = [2, 4, 4, 4, 5, 5, 5, 5, 6, 6]

# Calculate mean and standard deviation
mean = stats.mean(data)
std_dev = stats.stdev(data)

# Calculate Z-scores
z_scores = [(x - mean) / std_dev for x in data]

# Calculate relative z-scores
relative_z_scores = [z / std_dev for z in z_scores]

print(relative_z_scores)
