import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Load the iris dataset
iris = datasets.load_iris()

# We will use only features in our dataset
X = iris.data[:, :2]

# The target is the species
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the decision tree regressor
tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(X_train, y_train)

# Predict the test set results
y_pred = tree_reg.predict(X_test)

# Compute the mean squared error
mse = mean_squared_error(y_test, y_pred)
