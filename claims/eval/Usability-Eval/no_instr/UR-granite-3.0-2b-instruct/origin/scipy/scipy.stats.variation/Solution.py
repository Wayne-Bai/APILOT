import scipy.stats as stats

# Assuming 'data' is your dataset
data = [1, 2, 3, 4, 5]

# Calculate the mean
mean = stats.mean(data)

# Calculate the standard deviation
std_dev = stats.stdev(data)

# Calculate the coefficient of variation
cv = (std_dev / mean) if mean != 0 else 0

print("Coefficient of Variation: ", cv)
