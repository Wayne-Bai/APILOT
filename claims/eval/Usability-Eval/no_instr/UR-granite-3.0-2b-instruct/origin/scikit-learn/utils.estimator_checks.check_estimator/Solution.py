from sklearn import __version__
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

class CustomEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y):
        check_X_y(X, y, accept_sparse=True)
        self.X_ = X
        self.y_ = y
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X, ensure_2d=False)
        return X.dot(self.coef_)

    def score(self, X, y):
        check_X_y(X, y, accept_sparse=True)
        check_is_fitted(self)
        y_pred = self.predict(X)
        return accuracy_score(y, y_pred)
