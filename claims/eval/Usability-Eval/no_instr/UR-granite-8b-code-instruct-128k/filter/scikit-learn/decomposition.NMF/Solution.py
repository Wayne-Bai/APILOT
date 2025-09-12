from sklearn.decomposition import NMF
import numpy as np

# Generate a sample non-negative matrix X
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize NMF with n_components=2 (i.e. find two matrices W and H)
nmf = NMF(n_components=2, init='random', random_state=0)

# Fit the NMF model to the matrix X
W = nmf.fit_transform(X)

# Get the approximation of X using the factorization W and H
X_approx = nmf.components_.dot(nmf.transform(X))

# Print the original matrix X, the approximation X_approx, and the factorization matrices W and H
print("Original matrix X:")
print(X)
print("Approximation matrix X_approx:")
print(X_approx)
print("Factorization matrices W and H:")
print(W)
print(nmf.components_)
