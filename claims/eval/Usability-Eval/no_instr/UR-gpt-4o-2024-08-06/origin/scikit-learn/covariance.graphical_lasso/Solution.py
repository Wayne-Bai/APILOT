from sklearn.covariance import GraphicalLasso
import numpy as np

# Sample data
np.random.seed(0)
X = np.random.randn(100, 20)

# Fit the model
# Alpha controls the amount of regularization (L1 penalty)
model = GraphicalLasso(alpha=0.01)
model.fit(X)

# Get the covariance and precision matrices
covariance = model.covariance_
precision = model.precision_

print("Covariance matrix:\n", covariance)
print("Precision matrix:\n", precision)
