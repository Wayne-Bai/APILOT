import sklearn
from sklearn.base import BaseEstimator, RegressorMixin
from functools import wraps

def delegated_to_subestimator(attr):
    def delegator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return getattr(getattr(self, attr), func.__name__)(*args, **kwargs)
        return wrapper
    return delegator

class CustomEstimator(BaseEstimator, RegressorMixin):
    def __init__(self, sub_estimator):
        self.sub_estimator = sub_estimator

    @delegated_to_subestimator('sub_estimator')
    def predict(self, X):
        pass

    @delegated_to_subestimator('sub_estimator')
    def fit(self, X, y=None, **fit_params):
        pass

    @delegated_to_subestimator('sub_estimator')
    def score(self, X, y=None, sample_weight=None):
        pass
