from sklearn.decomposition import NMF
import numpy as np

# Sample non-negative matrix X
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Define the number of components
n_components = 2

# Create the NMF model
model = NMF(n_components=n_components, init='random', random_state=0)

# Fit the model to the data and transform the data
W = model.fit_transform(X)
H = model.components_

# Output the results
print("W (basis matrix):")
print(W)
print("\nH (coefficient matrix):")
print(H)
print("\nReconstructed X from W and H:")
print(np.dot(W, H))
