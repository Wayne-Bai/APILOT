from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data: 2D numpy array
data = np.array([[1.0, 2.0],
                 [3.0, 4.0],
                 [5.0, 6.0]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the StandardScaler on the data
scaler.fit(data)

# Transform the data: scale it
scaled_data = scaler.transform(data)

# Transform the scaled data back to its original space
original_data = scaler.inverse_transform(scaled_data)

# Print the original and transformed data
print("Original Data:\n", data)
print("Scaled Data:\n", scaled_data)
print("Inverse Transformed Data (Original Space):\n", original_data)
