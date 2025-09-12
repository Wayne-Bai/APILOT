import sklearn
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin, RegressorMixin
from sklearn.utils.validation import check_is_fitted

def delegates_to_sub_estimator(delegate):
    """Decorator for methods that delegate to a sub-estimator."""
    def wrapper(self, *args, **kwargs):
        # Make sure self.estimator is fitted
        check_is_fitted(self, ['estimator'])
        return delegate(self, *args, **kwargs)
    return wrapper

# Example usage with a simple custom estimator
class CustomEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self, estimator):
        self.estimator = estimator

    @delegates_to_sub_estimator
    def predict(self, X, **kwargs):
        return self.estimator.predict(X, **kwargs)
