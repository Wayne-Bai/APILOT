from sklearn.linear_model import LinearRegression
from sklearn.utils.validation import check_X_y
from scipy.stats import norm
import numpy as np

def bayesian_ard_regression(X, y, n_iter=1000, learning_rate=0.01, random_state=None):
    n_samples, n_features = X.shape
    lambda_ = np.ones(n_features)  # Initial lambda values
    alpha = 1.0  # Initial alpha value

    for _ in range(n_iter):
        # E-step: Compute the posterior distribution of the weights
        posterior = norm.pdf(X, scale=np.sqrt(lambda_ / alpha))

        # M-step: Update the lambda values
        lambda_ = (1 / alpha) * (X.T @ X / n_samples + lambda_ * posterior)

        # Update the alpha value
        alpha = 1.0 / (n_samples * np.sum(posterior))

    # Fit the linear regression model with the updated lambda values
    model = LinearRegression().fit(X, y, sample_weight=posterior)

    return model, lambda_, alpha
