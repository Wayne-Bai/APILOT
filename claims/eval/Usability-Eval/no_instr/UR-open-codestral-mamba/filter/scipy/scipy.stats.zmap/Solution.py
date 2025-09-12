import scipy.stats as stats

# Assuming we have a list of data
data = [1.5, 2.1, 2.6, 2.9, 3.5, 4.0, 4.6]

# Calculate the mean and standard deviation of the data
mean, std_dev = stats.norm.fit(data)

# Calculate relative z-scores
relative_z_scores = [(x - mean) / std_dev for x in data]

print("Relative z-scores: ", relative_z_scores)
