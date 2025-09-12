from sklearn.utils.estimator_checks import check_estimator
from sklearn.base import BaseEstimator

# Assuming we have defined our own estimator, let's call it MyEstimator
class MyEstimator(BaseEstimator):
    def __init__(self, param1=None):
        self.param1 = param1

    def fit(self, X, y=None):
        # Fit method implementation
        pass

    def predict(self, X):
        # Predict method implementation
        pass

# This will raise an exception if the estimator does not adhere to sklearn conventions.
results = check_estimator(MyEstimator)
