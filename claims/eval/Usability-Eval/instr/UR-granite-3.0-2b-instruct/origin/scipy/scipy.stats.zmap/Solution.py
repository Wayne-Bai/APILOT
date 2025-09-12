from scipy.stats import zscore

# Assuming 'data' is your dataset
data = [1, 2, 3, 4, 5]

# Calculate z-scores
z_scores = zscore(data)

# Print the relative z-scores
print(z_scores)
