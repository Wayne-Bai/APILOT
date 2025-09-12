
import numpy as np

# Generate a random signal
n_samples = 1000
n_features = 100
n_components = 10
density = 0.1

np.random.seed(42)
D = np.random.randn(n_components, n_features)
D /= np.linalg.norm(D, axis=1)[:, np.newaxis]

x = np.zeros((n_features, n_samples))
n_nonzero_coefs = int(n_features * density)

for i in range(n_samples):
    indices = np.random.choice(n_features, n_nonzero_coefs, replace=False)
    coef = np.random.randn(n_nonzero_coefs)
    x[:, i][indices] = coef

# Generate a signal as a sparse combination of dictionary elements
y = np.dot(D, x)

print(y)
