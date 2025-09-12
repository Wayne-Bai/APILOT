from sklearn.linear_model import LinearRegression
from sklearn.utils.validation import check_X_y
from scipy.stats import norm
import numpy as np

class BayesianARDRegression:
    def __init__(self, lambda_init=1.0, alpha_init=1.0):
        self.lambda_ = lambda_init
        self.alpha_ = alpha_init
        self.model = LinearRegression()

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.model.fit(X, y)

        # Compute residuals
        residuals = y - self.model.predict(X)

        # Compute initial values for lambda and alpha
        self.lambda_ = self.lambda_ * np.mean(np.abs(residuals))
        self.alpha = self.alpha * np.mean(np.square(residuals))

        # Evidence Maximization iteration
        while True:
            # Compute weights
            weights = norm.pdf(X, loc=0, scale=1/np.sqrt(self.lambda_))

            # Compute hyperparameters
            alpha_hat = self.alpha / np.sum(weights)
            lambda_hat = self.lambda_ / np.sum(weights**2)

            # Update lambda and alpha
            self.lambda_ = lambda_hat
            self.alpha = alpha_hat

            # Check convergence
            if np.abs(self.lambda_ - self.lambda_hat) < 1e-6 and np.abs(self.alpha - self.alpha_hat) < 1e-6:
                break

    def predict(self, X):
        X, _ = check_X_y(X, self.model.predict(X))
        weights = norm.pdf(X, loc=0, scale=1/np.sqrt(self.lambda_))
        return np.dot(weights, self.model.predict(X))
