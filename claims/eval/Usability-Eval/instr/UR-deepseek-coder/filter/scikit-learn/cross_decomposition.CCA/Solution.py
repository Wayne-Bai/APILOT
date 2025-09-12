import numpy as np
from sklearn.cross_decomposition import CCA

# Example data
X = np.random.rand(100, 10)  # 100 samples, 10 features
Y = np.random.rand(100, 5)   # 100 samples, 5 features

# Initialize CCA with the desired number of components
cca = CCA(n_components=2)

# Fit the model
cca.fit(X, Y)

# Transform the data to canonical components
X_c, Y_c = cca.transform(X, Y)

# Print the transformed components
print("Canonical components for X:")
print(X_c)
print("Canonical components for Y:")
print(Y_c)
