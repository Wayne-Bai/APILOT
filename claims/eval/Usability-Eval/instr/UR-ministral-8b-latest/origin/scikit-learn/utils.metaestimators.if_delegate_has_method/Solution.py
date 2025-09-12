import numpy as np
import random
from sklearn.base import BaseEstimator, ClassifierMixin, clone

class SubEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self, base_estimator):
        self.base_estimator = base_estimator

    def fit(self, X, y):
        self.base_estimator.fit(X, y)
        return self

    def predict(self, X):
        return self.base_estimator.predict(X)

    def predict_log_proba(self, X):
        return self.base_estimator.predict_log_proba(X)

# Example of a decorator to log calls to fit, predict, etc.
def log_method_call(method):
    def wrapper(self, *args, **kwargs):
        print(f"Calling {method.__name__} with args: {args} and kwargs: {kwargs}")
        return method(self, *args, **kwargs)
    return wrapper

# Applying the decorator to the fit method
@log_method_call
def fit_delegator(self, X, y):
    return self.base_estimator.fit(X, y)

@log_method_call
def predict_delegator(self, X):
    return self.base_estimator.predict(X)

# Injecting the decorated methods back into the class
SubEstimator.fit = fit_delegator
SubEstimator.predict = predict_delegator

# Example usage
if __name__ == "__main__":
    base_model = clone(random.RandomState(seed=0).random)

    sub_estimator = SubEstimator(base_model)

    X = np.random.rand(10, 20)
    y = np.random.randint(0, 2, size=10)

    sub_estimator.fit(X, y)
    predictions = sub_estimator.predict(X)
    print(predictions)
