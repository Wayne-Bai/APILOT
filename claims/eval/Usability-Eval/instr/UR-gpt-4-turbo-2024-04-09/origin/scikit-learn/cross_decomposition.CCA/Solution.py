import numpy as np
from sklearn.cross_decomposition import CCA

# Sample data
X = np.array([[0., 0., 1.], [1., 0., 0.], [2., 2., 2.], [3., 5., 4.]])
Y = np.array([[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]])

# Initialize CCA with number of components to learn from the data
cca = CCA(n_components=2)

# Fit and transform the data
cca.fit(X, Y)
X_c, Y_c = cca.transform(X, Y)

print("Transformed X:", X_c)
print("Transformed Y:", Y_c)
