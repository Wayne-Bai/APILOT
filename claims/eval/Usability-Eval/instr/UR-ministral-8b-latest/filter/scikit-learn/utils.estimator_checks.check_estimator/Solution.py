import sklearn.datasets

# Load the Iris dataset as an example
data = sklearn.datasets.load_iris()
X = data.data
y = data.target

# Check if the estimator adheres to scikit-learn conventions
# Import relevant modules for testing
from sklearn.base import BaseEstimator, ClassifierMixin

# Define a simple estimator that adheres to scikit-learn conventions
class SimpleEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self, param1):
        self.param1 = param1

    def fit(self, X, y):
        return self

    def predict(self, X):
        return y  # For simplicity, we return the input as prediction

# Create an instance of SimpleEstimator
estimator = SimpleEstimator(param1="example")

# Use scikit-learn's GridSearchCV to test the estimator
from sklearn.model_selection import GridSearchCV

# Example parameter grid
param_grid = {"param1": ["value1", "value2"]}

# Create a GridSearchCV object with cross-validation
grid_search = GridSearchCV(estimator, param_grid, cv=5, scoring='accuracy')

# Fit the model
grid_search.fit(X, y)

# Output the best parameters and best score
print("Best parameters:", grid_search.best_params_)
print("Best score:", grid_search.best_score_)
