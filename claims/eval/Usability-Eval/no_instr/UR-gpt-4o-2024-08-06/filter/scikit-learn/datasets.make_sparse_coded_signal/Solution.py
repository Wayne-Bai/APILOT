import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import OrthogonalMatchingPursuit

# Define parameters
n_features = 10
n_components = 5
n_samples = 3
n_nonzero_coefs = 2

# Create a dictionary matrix D
np.random.seed(0)
D = np.random.randn(n_features, n_components)

# Generate sparse code X with specified sparsity level
X = np.zeros((n_components, n_samples))
for i in range(n_samples):
    idx = np.random.choice(n_components, n_nonzero_coefs, replace=False)
    X[idx, i] = np.random.randn(n_nonzero_coefs)

# Calculate matrix Y as a product of D and X
Y = np.dot(D, X)

# Verification using Orthogonal Matching Pursuit (OMP)
omp = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs)
X_omp = np.zeros_like(X)

for i in range(Y.shape[1]):
    omp.fit(D, Y[:, i])
    X_omp[:, i] = omp.coef_

# Check if the reconstructed X is similar to the original X
print("Original X:\n", X)
print("Reconstructed X using OMP:\n", X_omp)
print("Are they approximately equal?", np.allclose(X, X_omp))
