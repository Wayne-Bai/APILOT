
from sklearn.tree import DecisionTreeRegressor

# Create a decision tree regressor
regressor = DecisionTreeRegressor()

# Fit the model to the training data
regressor.fit(X_train, y_train)

# Make predictions
predictions = regressor.predict(X_test)
