
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils import check_array

class DelegatingEstimator(BaseEstimator, TransformerMixin):
    def __init__(self, estimator, method):
        self.estimator = estimator
        self.method = method

    def fit(self, X, y=None, **fit_params):
        check_array(X)
        return self.estimator.fit(X, y, **fit_params)

    def transform(self, X):
        check_array(X)
        return getattr(self.estimator, self.method)(X)
