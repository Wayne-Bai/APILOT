from sklearn.base import BaseEstimator, clone
from functools import wraps

def delegated_decorator(delegated_class):
    """A decorator for methods that are delegated to a sub-estimator."""
    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, 'sub_estimator') or not isinstance(self.sub_estimator, delegated_class):
                raise AttributeError(f"This instance does not have a valid 'sub_estimator' of type {delegated_class.__name__}.")
            # Call the method on the sub-estimator
            return getattr(self.sub_estimator, method.__name__)(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
class DelegatingEstimator(BaseEstimator):
    def __init__(self, base_estimator, **kwargs):
        self.sub_estimator = clone(base_estimator)

    @delegated_decorator(BaseEstimator)
    def fit(self, X, y):
        pass

    @delegated_decorator(BaseEstimator)
    def predict(self, X):
        pass
