import numpy as np
from sklearn.covariance import GraphicalLasso
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin

class SparseInverseCovariance(BaseEstimator, TransformerMixin):
    def __init__(self, alphas=None, cv=5):
        self.alphas = alphas
        self.cv = cv

    def fit(self, X):
        if self.alphas is None:
            self.alphas = np.logspace(-2, 0, 20)

        param_grid = {'alpha': self.alphas}
        self.model_ = GridSearchCV(GraphicalLasso(), param_grid, cv=self.cv)
        self.model_.fit(X)
        return self

    def transform(self, X):
        return self.model_.covariance_

# Example usage:
# X = np.random.randn(100, 10)  # Example data
# sparse_inv_cov = SparseInverseCovariance()
# sparse_inv_cov.fit(X)
# cov_matrix = sparse_inv_cov.transform(X)
