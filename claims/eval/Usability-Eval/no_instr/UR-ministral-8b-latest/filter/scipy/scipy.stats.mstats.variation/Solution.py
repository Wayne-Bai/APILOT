import scipy.stats as stats

# Example data
data = [10, 15, 14, 12, 13, 16, 17, 11, 18, 19]

# Calculate the mean
mean = stats.mean(data)

# Calculate the standard deviation
std_dev = stats.pstdev(data)

# Calculate the coefficient of variation
cv = std_dev / mean

print(f'Coefficient of Variation: {cv:.2%}')
