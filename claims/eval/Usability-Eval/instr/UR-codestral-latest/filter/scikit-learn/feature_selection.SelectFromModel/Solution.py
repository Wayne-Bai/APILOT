from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectKBest, f_classif

class SelectImportantFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, k):
        self.k = k
        self.feature_selector = SelectKBest(score_func=f_classif, k=self.k)

    def fit(self, X, y=None):
        self.feature_selector.fit(X, y)
        return self

    def transform(self, X):
        return self.feature_selector.transform(X)

    def get_support(self):
        return self.feature_selector.get_support()
