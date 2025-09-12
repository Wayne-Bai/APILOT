
from sklearn.covariance import GraphicalLasso
import numpy as np

# Create a sample data matrix X
X = np.array([[0, 0], [1, 1], [2, 2]])

# Fit the GraphicalLasso estimator to the data
model = GraphicalLasso(alpha=0.01)
model.fit(X)

# Get the precision matrix (inverse of the covariance matrix)
precision_matrix = model.precision_

print("Precision matrix:")
print(precision_matrix)
