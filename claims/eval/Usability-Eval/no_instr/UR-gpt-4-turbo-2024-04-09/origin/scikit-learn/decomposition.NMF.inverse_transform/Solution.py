import numpy as np
from sklearn.preprocessing import StandardScaler

# Sample data
data = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# Initialize scaler
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Transform data back to its original space
original_data = scaler.inverse_transform(scaled_data)

print("Original Data:")
print(original_data)
