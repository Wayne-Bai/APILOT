import numpy as np
from sklearn.decomposition import NMF

# Sample non-negative dataset X
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Define the number of components
n_components = 2

# Initialize the NMF model
model = NMF(n_components=n_components, init='random', random_state=0)

# Fit the model to the data and transform it
W = model.fit_transform(X)

# Compute the components matrix
H = model.components_

# Display the resulting matrices
print("Matrix W (Basis matrix):")
print(W)
print("\nMatrix H (Coefficient matrix):")
print(H)

# The product W * H should approximate the original X
X_approx = np.dot(W, H)
print("\nApproximated X by W * H:")
print(X_approx)
