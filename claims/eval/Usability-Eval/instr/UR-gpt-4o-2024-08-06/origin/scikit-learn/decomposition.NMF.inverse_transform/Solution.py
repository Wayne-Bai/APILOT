from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
data = np.array([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]])

# Initialize a StandardScaler
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Inverse transform the scaled data to original space
original_data = (scaled_data * scaler.scale_) + scaler.mean_

print("Original data:\n", original_data)
