from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Sample data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Now, to transform back the scaled data to its original space
original_data = scaler.inverse_transform(scaled_data)

print("Original Data:")
print(original_data)
