# Import necessary libraries
from sklearn.cross_decomposition import CCA
import numpy as np

# Generate random data for demonstration
np.random.seed(0)
n = 100
X = np.random.normal(0, 1, (n, 5))  # 5 features for the first dataset
Y = np.random.normal(0, 1, (n, 4))  # 4 features for the second dataset

# Initialize and fit the CCA model
cca = CCA(n_components=2)  # Specify the number of components
cca.fit(X, Y)

# Print the explained covariance for each component
print("Explained covariance for each component:")
print(cca.explained_variance_ratio_)

# Transform the data using the learned projections
X_c, Y_c = cca.transform(X, Y)

# Print the shape of the transformed data
print("Shape of the transformed data:")
print(X_c.shape, Y_c.shape)

# Use the transformed data for further analysis or modeling
