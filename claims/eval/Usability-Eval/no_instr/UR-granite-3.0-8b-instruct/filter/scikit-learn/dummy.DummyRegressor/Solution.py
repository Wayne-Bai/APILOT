from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
import numpy as np

class SimpleRulesRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, rules):
        self.rules = rules

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.rules_ = self._fit_rules(X, y)
        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        return self._predict(X)

    def _fit_rules(self, X, y):
        rules = self.rules
        return rules

    def _predict(self, X):
        rules = self.rules_
        y_pred = np.zeros(X.shape[0])
        for rule in rules:
            y_pred[rule(X)] = rule.predict(X[rule(X)])
        return y_pred
