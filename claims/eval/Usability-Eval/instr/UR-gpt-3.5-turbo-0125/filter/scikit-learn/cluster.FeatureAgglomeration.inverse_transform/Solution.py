
from sklearn.base import BaseEstimator, TransformerMixin

class InverseTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, transformer):
        self.transformer = transformer

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.dot(self.transformer.inverse)
