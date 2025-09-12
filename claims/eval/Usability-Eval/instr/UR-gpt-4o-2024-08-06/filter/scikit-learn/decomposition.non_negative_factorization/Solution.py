import numpy as np
from sklearn.decomposition import NMF

# Create a non-negative matrix X
X = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Set the number of components you want
n_components = 2

# Initialize the NMF model
model = NMF(n_components=n_components, init='random', random_state=0)

# Fit the model and retrieve the matrices W and H
W = model.fit_transform(X)
H = model.components_

# Output the results
print("Original matrix (X):")
print(X)
print("\nMatrix W (after factorization):")
print(W)
print("\nMatrix H (after factorization):")
print(H)

# Verify the approximation
X_approx = np.dot(W, H)
print("\nApproximated matrix (W x H):")
print(X_approx)
