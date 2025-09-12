from sklearn.base import BaseEstimator, clone

def delegated_method(method_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, 'sub_estimator'):
                raise AttributeError("The 'sub_estimator' attribute is not set.")
            
            sub_estimator = getattr(self, 'sub_estimator')
            method = getattr(sub_estimator, method_name)
            return method(*args, **kwargs)
        
        return wrapper
    return decorator

class DelegatingEstimator(BaseEstimator):
    def __init__(self, sub_estimator):
        self.sub_estimator = sub_estimator

    @delegated_method('fit')
    def fit(self, X, y=None):
        pass

    @delegated_method('predict')
    def predict(self, X):
        pass

    @delegated_method('score')
    def score(self, X, y=None):
        pass

# Example usage:
from sklearn.linear_model import LinearRegression

model = DelegatingEstimator(sub_estimator=LinearRegression())
model.fit([[1, 2], [3, 4]], [1, 2])
predictions = model.predict([[1, 2], [3, 4]])
score = model.score([[1, 2], [3, 4]], [1, 2])
