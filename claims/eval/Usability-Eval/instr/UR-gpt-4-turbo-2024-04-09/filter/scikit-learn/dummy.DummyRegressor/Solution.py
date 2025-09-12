from sklearn.dummy import DummyRegressor

# Create a DummyRegressor object
dummy_regressor = DummyRegressor(strategy="mean")

# Assuming X_train, y_train have been defined and are available
# Fit the model
dummy_regressor.fit(X_train, y_train)

# Making predictions
predictions = dummy_regressor.predict(X_test)
