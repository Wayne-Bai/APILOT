import numpy as np

# Load data from a text file, handling missing values
data = np.genfromtxt('data.txt', delimiter=',', missing_values='NA', filling_values=np.nan)

# Display the loaded data
print(data)
