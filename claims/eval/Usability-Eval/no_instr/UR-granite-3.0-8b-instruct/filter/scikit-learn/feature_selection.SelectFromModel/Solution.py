from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class FeatureImportanceSelector(BaseEstimator, TransformerMixin):
    def __init__(self, n_features_to_select=5):
        self.n_features_to_select = n_features_to_select

    def fit(self, X, y):
        self.forest = RandomForestClassifier(n_estimators=100, random_state=0)
        self.forest.fit(X, y)
        self.feature_importances_ = self.forest.feature_importances_
        self.feature_names_ = X.columns
        return self

    def transform(self, X):
        sorted_idx = np.argsort(self.feature_importances_)[::-1]
        return X[:, sorted_idx[:self.n_features_to_select]]
