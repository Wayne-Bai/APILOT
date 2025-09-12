from scipy import stats
import numpy as np

# Generate sample data (assuming a normal distribution for demonstration)
np.random.seed(0)
data = np.random.normal(0, 1, 1000)

# Calculate the mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data, ddof=1)  # Use ddof=1 for sample standard deviation

# Compute the coefficient of variation (CV)
cv = std_dev / mean

print("Coefficient of Variation (CV):", cv)
