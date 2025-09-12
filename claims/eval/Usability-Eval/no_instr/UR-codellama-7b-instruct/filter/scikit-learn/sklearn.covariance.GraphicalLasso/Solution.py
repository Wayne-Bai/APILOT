
import numpy as np
from sklearn.covariance import OAS
from sklearn.linear_model import LassoLars

# Generate some random data for demonstration purposes
n_samples = 100
X = np.random.rand(n_samples, 10)

# Define the regularization parameter and the number of features to select
alpha = 0.5
k = 5

# Use OAS to estimate the sparse inverse covariance matrix
oas = OAS()
X_inv_cov = oas.fit(X)

# Use LassoLars to select the top k features based on the absolute value of the singular values of X_inv_cov
lasso_lars = LassoLars(alpha=alpha, n_nonzero_coefs=k)
selected_features = lasso_lars.fit(X_inv_cov).n_nonzero_coefs_

# Print the selected features and their corresponding singular values
print("Selected Features:")
for i, sv in enumerate(lasso_lars.singular_values_):
    print(f"Feature {i}: {sv}")
