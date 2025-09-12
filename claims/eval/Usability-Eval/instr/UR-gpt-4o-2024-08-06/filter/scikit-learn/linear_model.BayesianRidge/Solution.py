import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from scipy.stats import norm

# Generate synthetic data
np.random.seed(0)
n_samples, n_features = 100, 10
X = np.random.rand(n_samples, n_features)
true_coefs = np.random.randn(n_features)
y = X @ true_coefs + np.random.normal(scale=0.5, size=n_samples)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bayesian Ridge Regression using Ridge classifier as a proxy
class BayesianRidge:
    def __init__(self, alpha_1=1e-6, alpha_2=1e-6, lambda_1=1e-6, lambda_2=1e-6, tol=1e-3):
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2
        self.lambda_1 = lambda_1
        self.lambda_2 = lambda_2
        self.tol = tol
        self.alpha_ = None
        self.lambda_ = None
        self.coef_ = None
        self.model_ = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Start with an initial guess for alpha and lambda
        alpha_ = self.alpha_1 / self.alpha_2
        lambda_ = self.lambda_1 / self.lambda_2

        converged = False
        coef_ = np.zeros(n_features)

        while not converged:
            # Use Ridge Regression to estimate the weights
            self.model_ = Ridge(alpha=lambda_, fit_intercept=False, tol=self.tol)
            self.model_.fit(X, y)
            coef_ = self.model_.coef_
            
            # Estimate the variance of the weights
            lambda_ = (n_features + 2 * self.lambda_1) / (np.sum(coef_ ** 2) + 2 * self.lambda_2)
            # Calculate the variance of the residual error
            residual = y - X @ coef_
            gamma = np.sum(coef_ ** 2)
            alpha_ = (n_samples + 2 * self.alpha_1) / (np.sum(residual ** 2) + gamma + 2 * self.alpha_2)
            
            # Check for convergence
            converged = np.abs(alpha_ - self.alpha_) < self.tol and np.abs(lambda_ - self.lambda_) < self.tol
            self.alpha_ = alpha_
            self.lambda_ = lambda_

        self.coef_ = coef_

    def predict(self, X):
        return X @ self.coef_

# Create an instance of the BayesianRidge and fit it to the data
bayesian_ridge = BayesianRidge()
bayesian_ridge.fit(X_train, y_train)

# Predict on new data
y_pred = bayesian_ridge.predict(X_test)

# Print out some results
print("Coefficients:", bayesian_ridge.coef_)
print("Alpha (precision of the noise):", bayesian_ridge.alpha_)
print("Lambda (precision of the weights):", bayesian_ridge.lambda_)
