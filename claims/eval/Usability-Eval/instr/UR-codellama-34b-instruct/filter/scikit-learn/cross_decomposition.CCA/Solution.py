
from sklearn.cross_decomposition import CCA
import numpy as np

# Generate some random data for demonstration purposes
np.random.seed(0)
X = np.random.rand(10, 5)
Y = np.random.rand(10, 4)

# Perform CCA
cca = CCA(n_components=3)
cca.fit([X, Y])

# Extract the canonical variables
X_canonical = cca.transform(X)
Y_canonical = cca.transform(Y)

print("Canonical variables:")
print(X_canonical)
print(Y_canonical)
