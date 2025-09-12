from sklearn.decomposition import NMF
import numpy as np

# Sample non-negative data matrix X
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

# Initialize the NMF model
n_components = 2  # Number of latent features
model = NMF(n_components=n_components, init='random', random_state=42)

# Fit the model to the data
W = model.fit_transform(X)
H = model.components_

print("Original Matrix (X):")
print(X)
print("\nW Matrix:")
print(W)
print("\nH Matrix:")
print(H)

# Verify the approximation
approximation = np.dot(W, H)
print("\nProduct of W and H, approximating X:")
print(approximation)
