import numpy as np
from sklearn.cross_decomposition import CCA

# Sample data
X = np.array([[0., 0., 1.], [1., 0., 0.], [0., 1., 0.], [1., 1., 1.]])
Y = np.array([[1., 0., 0.], [0., 1., 1.], [1., 1., 0.], [0., 0., 1.]])

# Create a CCA object
cca = CCA(n_components=2)

# Fit the model on the data
cca.fit(X, Y)

# Transform the data
X_c, Y_c = cca.transform(X, Y)

print("Transformed X:\n", X_c)
print("Transformed Y:\n", Y_c)
