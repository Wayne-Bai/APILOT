# Importing necessary libraries
from sklearn.covariance import graph_lasso
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np
import matplotlib.pyplot as plt

# Generate random data for the purpose of demonstration
n_samples = 100
n_features = 20

ensemble_cov = make_sparse_spd_matrix(n_features, alpha=0.9, normed_diag=True, succinct=False)
ensemble_cov = ensemble_cov + np.eye(n_features)  # Add identity matrix to make it invertible


# Create a sample dataset with the given covariance matrix
ensemble_data = np.random.multivariate_normal(ensemble_cov);

# Calculate the sample covariance matrix
sample_cov = np.cov(ensemble_data.T)


# Perform sparse inverse covariance estimation using the l1-penalized estimator
l1_lambda_res = np.linspace(0, 1, 100)  # Range of lambda values
emp_cov_lasso = graph_lasso.CovarianceLasso(n_jobs=-1).fit(sample_cov, alphas=l1_lambda_res)


# Extract the inverse covariance estimates for the minimum lambda
l1_lambda = emp_cov_lasso.lambda_max / 1.1  # Reduce overfitting
l1_emp_cov = emp_cov_lasso.fit(sample_cov, alphas=l1_lambda)


# Print the estimated inverse covariance matrix
print(l1_emp_cov.covariance_)
