from sklearn.preprocessing import StandardScaler
import numpy as np

# Example data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Inverse the transformation
original_data = scaler.inverse_transform(scaled_data)

print("Original Data:\n", original_data)
