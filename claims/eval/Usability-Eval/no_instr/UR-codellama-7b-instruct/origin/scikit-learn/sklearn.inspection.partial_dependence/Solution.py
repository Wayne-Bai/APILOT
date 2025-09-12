
import numpy as np
from sklearn import tree

# Define the data
X = [[0, 0], [1, 1]]
y = [0, 1]

# Create a decision tree regressor
regressor = tree.DecisionTreeRegressor()

# Fit the model to the data
regressor.fit(X, y)

# Get the partial dependence of the first feature
pd = regressor.partial_dependence(0)
print("Partial dependence of first feature:", pd)

# Get the partial dependence of both features
pds = regressor.partial_dependence(np.array([0, 1]))
print("Partial dependence of both features:", pds)
