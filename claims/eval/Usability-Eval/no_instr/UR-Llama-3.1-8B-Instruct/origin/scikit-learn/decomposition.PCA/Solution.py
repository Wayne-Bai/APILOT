# Import the necessary libraries
from sklearn.decomposition import PCA
import numpy as np

# Generate random data for demonstration purposes
np.random.seed(0)
data = np.random.rand(100, 10)

# Create a PCA instance with 2 components (i.e., we're reducing the dimensionality to 2)
pca = PCA(n_components=2)

# Fit the PCA instance to the data
pca.fit(data)

# Transform the data to the new 2-dimensional space
new_data = pca.transform(data)

print(new_data.shape)  # Output: (100, 2)
