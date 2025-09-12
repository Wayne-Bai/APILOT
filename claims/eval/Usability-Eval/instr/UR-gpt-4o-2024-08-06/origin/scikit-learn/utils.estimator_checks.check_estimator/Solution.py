from sklearn.utils.estimator_checks import parametrize_with_checks
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class CustomClassifier(BaseEstimator, ClassifierMixin):
    def fit(self, X, y):
        # Sample fitting code
        self.classes_, y = np.unique(y, return_inverse=True)
        return self

    def predict(self, X):
        # Sample prediction code
        return np.zeros(X.shape[0], dtype=int)

@parametrize_with_checks([CustomClassifier()])
def test_sklearn_conventions(estimator, check):
    check(estimator)
