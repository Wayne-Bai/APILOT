from sklearn.base import BaseEstimator, TransformerMixin

class Subestimator:
    def __init__(self, estimator):
        self.estimator = estimator

    def fit(self, X, y=None):
        return self.estimator.fit(X, y)

    def transform(self, X):
        return self.estimator.transform(X)

def delegate_method(method_name):
    def decorator(func):
        func.delegate = Subestimator(func.estimator)
        return func

    return decorator

class MyEstimator(BaseEstimator, TransformerMixin):
    def __init__(self, estimator):
        self.estimator = estimator

    @delegate_method('fit')
    def fit(self, X, y=None):
        return super().fit(X, y)

    @delegate_method('transform')
    def transform(self, X):
        return super().transform(X)
