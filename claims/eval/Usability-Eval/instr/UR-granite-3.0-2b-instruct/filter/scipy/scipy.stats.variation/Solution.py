from scipy import stats

# Assuming 'data' is your dataset
data = [1, 2, 3, 4, 5]

# Compute the mean
mean = stats.moment(data, moment=1, axis=None)

# Compute the standard deviation
std_dev = stats.moment(data, moment=2, axis=None, ddof=1)

# Compute the coefficient of variation
cv = (std_dev / mean) if mean != 0 else float('inf')

print("Coefficient of Variation: ", cv)
