from sklearn import base
from sklearn.utils.validation import check_X_y, check_is_fitted

class CustomEstimator(base.BaseEstimator):
    def __init__(self):
        self.X = None
        self.y = None

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.X = X
        self.y = y
        return self

    def predict(self, X):
        check_is_fitted(self)
        return X

    def score(self, X, y):
        check_is_fitted(self)
        return 1.0
