from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define a function to calculate feature importance
def calculate_importance(X, y):
    model = LinearRegression()
    model.fit(X, y)
    importance = np.abs(model.coef_)
    return importance

# Calculate feature importance
importance = calculate_importance(X, y)

# Select top 2 features based on importance
selector = SelectKBest(score_func=lambda x: np.sum(x), k=2)
X_new = selector.fit_transform(X, y)

# Print the selected features
print("Selected features:", np.argsort(importance)[-2:])
