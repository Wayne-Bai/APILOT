from sklearn.tree import DecisionTreeRegressor

# Create a decision tree regressor object
regressor = DecisionTreeRegressor()

# Fit the regressor to the data
regressor.fit(X_train, y_train)

# Predict the target variable for new instances
y_pred = regressor.predict(X_test)
