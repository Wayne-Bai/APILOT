
import numpy as np
from sklearn.cross_decomposition import CCA

# Generate some sample data
X = np.random.rand(100, 5)
Y = np.random.rand(100, 5)

# Perform CCA
cca = CCA(n_components=2)
cca.fit(X, Y)

# Extract the canonical variables
X_canonical = cca.transform(X)
Y_canonical = cca.transform(Y)

print("Canonical variables for X:")
print(X_canonical)
print("Canonical variables for Y:")
print(Y_canonical)
