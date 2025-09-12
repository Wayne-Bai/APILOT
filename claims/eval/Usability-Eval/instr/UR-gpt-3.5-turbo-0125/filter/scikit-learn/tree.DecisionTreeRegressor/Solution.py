
from sklearn.tree import DecisionTreeRegressor

# Create a decision tree regressor object
regressor = DecisionTreeRegressor()

# Fit the model using X_train as training data and y_train as target values
regressor.fit(X_train, y_train)

# Predict the target value based on X_test
predictions = regressor.predict(X_test)
