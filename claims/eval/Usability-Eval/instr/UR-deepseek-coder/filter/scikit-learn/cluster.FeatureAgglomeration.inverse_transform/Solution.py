import numpy as np
from sklearn.preprocessing import StandardScaler

# Example data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
transformed_data = scaler.fit_transform(data)

# Inverse the transformation
inverse_transformed_data = scaler.inverse_transform(transformed_data)

print("Original Data:\n", data)
print("Transformed Data:\n", transformed_data)
print("Inverse Transformed Data:\n", inverse_transformed_data)
