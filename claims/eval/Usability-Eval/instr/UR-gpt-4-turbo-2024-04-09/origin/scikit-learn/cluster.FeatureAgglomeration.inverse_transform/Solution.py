# Import the necessary packages from sklearn
from sklearn.preprocessing import StandardScaler
import numpy as np

# Simulate some data
data = np.array([[1.0, -1.0, 2.0],
                 [2.0, 0.0, 0.0],
                 [0.0, 1.0, -1.0]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Inverse the transformation to get the original data back
original_data = scaler.inverse_transform(scaled_data)

print("Original Data:")
print(original_data)
