from sklearn.decomposition import NMF
import numpy as np

# Example input matrix X
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=float)

# Initialize the NMF model
nmf = NMF(n_components=2, init='random', random_state=42)

# Fit the model
W = nmf.fit_transform(X)
H = nmf.components_

print("Weight Matrix W:")
print(W)
print("\nMatrix H:")
print(H)
