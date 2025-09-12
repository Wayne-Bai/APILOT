from scipy import stats
import numpy as np

# Generate a random dataset for demonstration
np.random.seed(0)
data = np.random.randn(100)

# Calculate the standard deviation of the data
std_dev = stats.tstd(data)

# Calculate the mean of the data
mean = stats.tmean(data)

# Calculate the coefficient of variation
cv = (std_dev / mean) * 100

print("Coefficient of Variation: ", cv)
