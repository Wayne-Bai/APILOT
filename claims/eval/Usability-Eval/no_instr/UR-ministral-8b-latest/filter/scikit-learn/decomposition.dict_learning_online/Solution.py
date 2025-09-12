from sklearn.decomposition import NMF
import numpy as np

# Example data: a 4x6 dictionary with 24 terms
# Replace this with your own matrix
X = np.array([[1.0, 2.0, 3.0, 4.0],
              [4.0, 5.0, 6.0, 7.0],
              [7.0, 8.0, 9.0, 10.0],
              [10.0, 11.0, 12.0, 13.0],
              [2.0, 3.0, 4.0, 5.0],
              [5.0, 6.0, 7.0, 8.0],
              [8.0, 9.0, 10.0, 11.0],
              [11.0, 12.0, 13.0, 14.0],
              [3.0, 4.0, 5.0, 6.0],
              [6.0, 7.0, 8.0, 9.0]])

# Initialize the NMF model
nmf = NMF(n_components=3, max_iter=200, random_state=0)

# Fit the NMF model on the data
W = nmf.fit_transform(X)

# Obtain the basis coefficients
H = nmf.components_

# Reconstruct the data
reconstructed = np.dot(W, H)

print("Original Data:\n", X)
print("\nReconstructed Data:\n", reconstructed)
