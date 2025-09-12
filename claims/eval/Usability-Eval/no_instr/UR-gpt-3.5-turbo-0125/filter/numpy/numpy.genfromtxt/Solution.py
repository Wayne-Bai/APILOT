
import numpy as np

# Load data from text file with missing values handled as NaN
data = np.genfromtxt('data.txt', delimiter=',', missing_values='NA', filling_values=np.nan)

print(data)
