# Importing necessary libraries
from sklearn.decomposition import NMF
import numpy as np

# Example non-negative matrix X
X = np.array([[1, 0, 3],
              [3, 5, 1],
              [4, 2, 2]])

# Setting the number of components for the factorization
n_components = 2

# Initializing the NMF model
model = NMF(n_components=n_components, init='random', random_state=0)

# Fit the model to the data matrix X
W = model.fit_transform(X)

# Obtain the H matrix
H = model.components_

# Output the results
print("W matrix:")
print(W)

print("H matrix:")
print(H)

# Approximate X again to check the factorization
X_approx = np.dot(W, H)
print("Approximated X:")
print(X_approx)
