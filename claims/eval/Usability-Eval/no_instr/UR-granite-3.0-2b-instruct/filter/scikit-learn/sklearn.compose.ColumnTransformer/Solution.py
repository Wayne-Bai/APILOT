from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_X_y

class Transformer(TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        X, y = check_X_y(X, y)
        return self

    def transform(self, X):
        return X[self.columns]
