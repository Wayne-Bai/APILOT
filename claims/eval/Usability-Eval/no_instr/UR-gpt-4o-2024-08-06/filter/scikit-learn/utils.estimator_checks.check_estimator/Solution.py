import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.estimator_checks import check_estimator

# Creating a mock estimator class for the purpose of this example
class MockEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self, param1=1):
        self.param1 = param1

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = self._validate_data(X, y, accept_sparse=True)
        self.classes_ = np.unique(y)
        return self

    def predict(self, X):
        # Simple prediction method (does not actually predict correctly)
        check_is_fitted(self, 'classes_')
        X = self._validate_data(X, accept_sparse=True)
        return np.repeat(self.classes_[0], X.shape[0])

    def score(self, X, y):
        from sklearn.metrics import accuracy_score
        return accuracy_score(y, self.predict(X))

# Check if the mock estimator adheres to the scikit-learn conventions
check_estimator(MockEstimator())
