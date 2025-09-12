from sklearn.ensemble import ExtraTreesRegressor

# Create an instance of the regressor
regressor = ExtraTreesRegressor()

# Fit the model to the data
regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regressor.predict(X_test)
