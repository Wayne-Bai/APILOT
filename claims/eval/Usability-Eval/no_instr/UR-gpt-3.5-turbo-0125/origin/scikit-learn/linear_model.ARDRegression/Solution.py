
import numpy as np

class BayesianARDRegression:
    def __init__(self, alpha=1.0, beta=1.0):
        self.alpha = alpha
        self.beta = beta

    def fit(self, X, y, max_iter=100, tol=1e-6):
        n_samples, n_features = X.shape
        self.alpha = np.full(n_features, self.alpha)
        self.beta = self.beta
        XX = np.dot(X.T, X)
        Xy = np.dot(X.T, y)

        for _ in range(max_iter):
            alpha = self.alpha
            beta = self.beta

            # Update the weight precision parameters
            gamma = 1 - alpha * np.diag(XX)
            self.alpha = np.sum((beta * gamma) / (beta + gamma))

            # Update weights
            w_mean = beta * np.dot(np.linalg.inv(np.diag(alpha) + beta * XX), Xy)
    
            # Update noise precision parameter
            self.beta = (n_samples - np.sum(gamma)) / np.sum(np.square(y - np.dot(X, w_mean)))

            if np.sum((self.alpha - alpha) ** 2) + (self.beta - beta) ** 2 < tol:
                break

    def predict(self, X):
        return np.dot(X, self.w_mean)
