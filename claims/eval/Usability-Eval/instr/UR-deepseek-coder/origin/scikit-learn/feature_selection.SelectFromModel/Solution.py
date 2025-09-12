import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier

class MetaTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, estimator=RandomForestClassifier(n_estimators=100), threshold=None):
        self.estimator = estimator
        self.threshold = threshold

    def fit(self, X, y):
        self.estimator.fit(X, y)
        return self

    def transform(self, X):
        selector = SelectFromModel(self.estimator, threshold=self.threshold)
        selector.fit(X)
        return selector.transform(X)

# Example usage:
# X_train, y_train = ...
# X_test = ...
# meta_transformer = MetaTransformer()
# X_train_transformed = meta_transformer.fit_transform(X_train, y_train)
# X_test_transformed = meta_transformer.transform(X_test)
