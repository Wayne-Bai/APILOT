import scipy.stats as stats

# Assume that data is a list of numerical values
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate the mean of the data
mean = stats.mean(data)

# Calculate the standard deviation of the data
std_dev = stats.stdev(data)

# Calculate the coefficient of variation
cv = (std_dev / mean) * 100

print("The coefficient of variation is:", cv)
