from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier

class ImportanceFeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, estimator=RandomForestClassifier()):
        self.estimator = estimator

    def fit(self, X, y=None):
        self.estimator.fit(X, y)
        return self

    def transform(self, X, y=None):
        importances = self.estimator.feature_importances_
        indices = np.argsort(importances)[::-1]

        top_features = indices[:self.top_n]
        return X[:, top_features]

    def set_params(self, **params):
        self.top_n = params.pop('top_n', 5)
        return self

# Example usage
selector = ImportanceFeatureSelector()
selector.fit(X_train, y_train)
X_train_selected = selector.transform(X_train)
X_test_selected = selector.transform(X_test)
