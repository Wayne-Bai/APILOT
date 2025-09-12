
import numpy as np
from sklearn import linear_model

# Generate random dictionary and sparse signal
n_samples, n_features, n_components = 100, 100, 10
np.random.seed(0)
D = np.random.randn(n_features, n_components)
X = np.zeros((n_samples, n_features))
support = np.random.choice(n_features, n_components, replace=False)
for i in range(n_components):
    X[:, support[i]] = np.random.randn(n_samples)

# Solve the sparse coding problem
lars = linear_model.Lars(n_nonzero_coefs=n_components)
lars.fit(D, X.T)

# Display the results
print("Dictionary:")
print(D)
print("\nSparse Code:")
print(lars.coef_)
