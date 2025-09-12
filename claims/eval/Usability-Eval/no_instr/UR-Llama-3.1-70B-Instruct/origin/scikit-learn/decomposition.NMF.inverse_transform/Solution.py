# Import necessary libraries
from sklearn.decomposition import PCA
import numpy as np

# Generate a random dataset
np.random.seed(0)
data = np.random.rand(100, 3)

# Create a PCA instance and fit the data
pca = PCA(n_components=2)
transformed_data = pca.fit_transform(data)

# Transform data back to its original space
inverse_transformed_data = pca.inverse_transform(transformed_data)

# Print the first 5 rows of original and inverse transformed data
print("Original Data:")
print(data[:5])
print("\nInverse Transformed Data:")
print(inverse_transformed_data[:5])
