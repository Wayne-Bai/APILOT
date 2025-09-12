# Import necessary modules from scikit-learn
from sklearn.base import BaseEstimator
from sklearn.utils.estimator_checks import check_estimator

# Define a class MyEstimator that inherits from BaseEstimator
class MyEstimator(BaseEstimator):
    def __init__(self, param1=None, param2=None):
        self.param1 = param1
        self.param2 = param2

    def fit(self, X, y=None):
        # This method should fit the data
        return self

    def predict(self, X):
        # This method should make predictions based on the fitted model
        return X * self.param1

# Create an instance of MyEstimator
estimator = MyEstimator(param1=2, param2=3)

# Check if the MyEstimator adheres to scikit-learn conventions
try:
    check_estimator(estimator)
except Exception as e:
    print(f"Estimator does not adhere to scikit-learn conventions: {e}")

# Example usage:
X = [[1], [2], [3]]
y = [4, 5, 6]

estimator.fit(X, y)
predictions = estimator.predict(X)
print(f"Predictions: {predictions}")
