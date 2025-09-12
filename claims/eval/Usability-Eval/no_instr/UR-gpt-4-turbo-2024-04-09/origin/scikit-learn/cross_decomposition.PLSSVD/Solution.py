import numpy as np
from sklearn.cross_decomposition import PLSSVD

# Example data
X = np.array([[0., 0., 1.], [1., 0., 0.], [2., 2., 2.], [3., 5., 4.]])
Y = np.array([[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]])

# Create a PLSSVD model
plssvd = PLSSVD(n_components=2)

# Fit the model
plssvd.fit(X, Y)

# Transform the data
X_c, Y_c = plssvd.transform(X, Y)

# Access singular values
singular_values = plssvd.singular_values_

# Print outputs
print("Transformed X:", X_c)
print("Transformed Y:", Y_c)
print("Singular values:", singular_values)
