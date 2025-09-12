import inspect
from functools import wraps
from sklearn.base import BaseEstimator

def delegate_to_sub_estimator(sub_estimator_attr):
    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            sub_estimator = getattr(self, sub_estimator_attr)
            if not isinstance(sub_estimator, BaseEstimator):
                raise ValueError(f"{sub_estimator_attr} is not a valid sub-estimator.")
            sub_method = getattr(sub_estimator, method.__name__)
            if not callable(sub_method):
                raise AttributeError(f"{method.__name__} is not a method of the sub-estimator.")
            return sub_method(*args, **kwargs)
        return wrapper
    return decorator

# Example usage:
class MyEstimator(BaseEstimator):
    def __init__(self, sub_estimator):
        self.sub_estimator = sub_estimator
    
    @delegate_to_sub_estimator('sub_estimator')
    def fit(self, X, y):
        pass

    @delegate_to_sub_estimator('sub_estimator')
    def predict(self, X):
        pass
        
# Usage Example
from sklearn.linear_model import LinearRegression

sub_estimator = LinearRegression()
my_estimator = MyEstimator(sub_estimator)

# Now my_estimator.fit and my_estimator.predict are delegated to sub_estimator's methods
my_estimator.fit([[1, 2], [3, 4]], [5, 6])
predictions = my_estimator.predict([[1, 2]])
