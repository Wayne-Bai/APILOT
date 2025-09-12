import numpy as np
from sklearn.covariance import GraphicalLasso
from sklearn.datasets import make_sparse_spd_matrix

# Generate a sparse symmetric positive definite matrix
true_cov = make_sparse_spd_matrix(dim=5, alpha=0.95, random_state=42)
X = np.random.multivariate_normal(mean=np.zeros(5), cov=true_cov, size=200)

# Instantiate the GraphicalLasso estimator
model = GraphicalLasso(alpha=0.1, max_iter=1000, verbose=True)

# Fit the model to the data
model.fit(X)

# Estimated covariance matrix
estimated_covariance = model.covariance_

# Estimated precision (inverse covariance) matrix
estimated_precision = model.precision_

print("Estimated Covariance:")
print(estimated_covariance)
print("\nEstimated Precision (Inverse Covariance):")
print(estimated_precision)
