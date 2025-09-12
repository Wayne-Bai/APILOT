from sklearn.base import BaseEstimator

def requires_sklearn_model(func):
    def wrapper(self, *args, **kwargs):
        if not isinstance(self.estimator, BaseEstimator):
            raise TypeError("Requires scikit-learn estimator as class attribute 'estimator'")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    def __init__(self, estimator):
        self.estimator = estimator

    @requires_sklearn_model
    def my_method(self):
        # Method logic here
        pass
