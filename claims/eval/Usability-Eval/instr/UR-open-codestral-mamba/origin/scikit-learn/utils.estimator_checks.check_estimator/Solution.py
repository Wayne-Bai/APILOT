import sklearn
from sklearn.base import check_estimator

# Creating a dummy estimator for the demonstration
class DummyEstimator:
    def fit(self, X, y):
        return self
    def predict(self, X):
        return X
# Now we can pass the estimator to the check function
check_estimator(DummyEstimator())
