from sklearn.base import BaseEstimator, TransformerMixin

class Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.columns].apply(lambda x: x.transform(), axis=0)
