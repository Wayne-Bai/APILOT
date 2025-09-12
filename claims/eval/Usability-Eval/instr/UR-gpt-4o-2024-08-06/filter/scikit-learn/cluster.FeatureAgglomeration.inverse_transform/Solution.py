import numpy as np
from sklearn.preprocessing import StandardScaler

# Create some example data
data = np.array([[1, 2], 
                 [3, 4], 
                 [5, 6]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler and transform the data
scaled_data = scaler.fit_transform(data)

# Invert the transformation
# We use the mean and the scale of each feature to inverse the transformation
inverted_data = scaled_data * scaler.scale_ + scaler.mean_

print("Original Data:")
print(data)
print("\nScaled Data:")
print(scaled_data)
print("\nInverted Data:")
print(inverted_data)
