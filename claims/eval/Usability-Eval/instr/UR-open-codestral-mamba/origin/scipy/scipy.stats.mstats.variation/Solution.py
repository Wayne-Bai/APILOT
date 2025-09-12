import scipy.stats as stats
import numpy as np

# Assuming we have a sample data
data = np.array([10, 12, 12, 15, 20, 22, 22, 22, 25, 30])

# Computing mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Computing coefficient of variation
cv = std_dev / mean

print(f'Coefficient of variation: {cv}')
