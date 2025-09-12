from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class Subestimator:
    def __init__(self):
        self.is_fitted = False

    def fit(self, X, y):
        check_X_y(X, y, accept_sparse=True)
        self.X = X
        self.y = y
        self.is_fitted = True
        return self

    def predict(self, X):
        check_is_fitted(self)
        if not self.is_fitted:
            raise NotFittedError("Estimator is not fitted yet")
        return self.X.dot(X)

class SubestimatorDecorator(BaseEstimator, RegressorMixin, ClassifierMixin):
    def __init__(self, subestimator):
        self.subestimator = subestimator

    def fit(self, X, y):
        self.subestimator.fit(X, y)
        return self

    def predict(self, X):
        return self.subestimator.predict(X)

    def decision_function(self, X):
        return self.subestimator.predict(X)
