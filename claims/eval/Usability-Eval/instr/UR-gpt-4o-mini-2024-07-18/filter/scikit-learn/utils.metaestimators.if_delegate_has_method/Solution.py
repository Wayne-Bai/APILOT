import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

def delegate_to_subestimator(method_name):
    """Decorator to delegate method calls to a sub-estimator."""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Check if the sub-estimator exists
            if not hasattr(self, '_sub_estimator'):
                raise AttributeError("Sub-estimator not set.")
            sub_estimator = getattr(self, '_sub_estimator')
            # Call the method on the sub-estimator
            method = getattr(sub_estimator, method_name)
            return method(*args, **kwargs)
        return wrapper
    return decorator

class MyCompositeEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self, sub_estimator):
        self._sub_estimator = sub_estimator

    @delegate_to_subestimator('fit')
    def fit(self, X, y):
        pass  # Delegated to the sub-estimator

    @delegate_to_subestimator('score')
    def score(self, X, y):
        pass  # Delegated to the sub-estimator

# Usage example

from sklearn.linear_model import LogisticRegression

# Create a composite estimator with a Logistic Regression as the sub-estimator
log_reg = LogisticRegression()
composite_estimator = MyCompositeEstimator(sub_estimator=log_reg)

# Now you can use fit and score methods which are delegated to log_reg
X = np.array([[0, 0], [1, 1]])
y = np.array([0, 1])
composite_estimator.fit(X, y)
print(composite_estimator.score(X, y))
