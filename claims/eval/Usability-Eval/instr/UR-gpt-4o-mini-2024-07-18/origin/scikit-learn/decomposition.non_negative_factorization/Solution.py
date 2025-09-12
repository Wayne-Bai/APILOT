import numpy as np
from sklearn.decomposition import NMF

# Generate a non-negative matrix X (example data)
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Set the number of components for the NMF
n_components = 2

# Create an NMF model
model = NMF(n_components=n_components, init='random', random_state=0)

# Fit the model and transform the data
W = model.fit_transform(X)
H = model.components_

# Display the results
print("Original Matrix X:")
print(X)
print("\nMatrix W:")
print(W)
print("\nMatrix H:")
print(H)
print("\nApproximated Matrix X (W * H):")
print(np.dot(W, H))
