
from sklearn import ensemble
from sklearn import datasets
import numpy as np

# Load the boston housing dataset
boston = datasets.load_boston()
X = boston.data
y = boston.target

# Create an extremely randomized tree regressor with 100 decision trees
regressor = ensemble.ExtraTreesRegressor(n_estimators=100, random_state=42)

# Fit the model to the data
regressor.fit(X, y)

# Print the R-squared score for the test set
print(regressor.score(X, y))
