from sklearn.covariance import EmpiricalCovariance
from sklearn.linear_model import Lasso
import numpy as np

class L1PenalizedCovariance(EmpiricalCovariance):
    def __init__(self, alpha=0.1, copy=True):
        self.alpha = alpha
        self.copy_ = copy
        self.covariance_ = None

    def fit(self, X):
        X = np.asarray(X)
        n_samples, n_features = X.shape

        # Compute the initial covariance matrix
        initial_covariance = super(L1PenalizedCovariance, self).fit(X).covariance_

        # Initialize the L1-penalized covariance matrix
        self.covariance_ = initial_covariance.copy()

        # Perform L1-regularized covariance estimation
        for i in range(n_features):
            for j in range(i, n_features):
                self.covariance_[i, j] = Lasso(alpha=self.alpha).fit(X[:, [i, j]].T, self.covariance_[i, j]).coef_[0]

        return self
