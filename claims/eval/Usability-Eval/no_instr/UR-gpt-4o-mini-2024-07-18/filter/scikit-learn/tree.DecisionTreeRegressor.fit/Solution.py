import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the decision tree regressor
regressor = DecisionTreeRegressor()

# Fitting the model on the training set
regressor.fit(X_train, y_train)

# You can now use regressor to make predictions
predictions = regressor.predict(X_test)
