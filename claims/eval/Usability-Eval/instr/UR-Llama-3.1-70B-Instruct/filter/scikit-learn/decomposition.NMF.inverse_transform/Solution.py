# Import necessary libraries
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample dataset
data = np.array([[1., -2., 3., 4.],
                 [5., 6., -1., -2.],
                 [-3., -4., 5., 6.]])

# Create a StandardScaler object
scaler = StandardScaler()

# Fit and transform the data to standardized space
data_standardized = scaler.fit_transform(data)

# Transform data back to its original space
data_original = scaler.inverse_transform(data_standardized)

# Print the results
print("Original Data:")
print(data)
print("Standardized Data:")
print(data_standardized)
print("Transformed back to original space:")
print(data_original)
