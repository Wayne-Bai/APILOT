from sklearn.ensemble import ExtraTreesRegressor

# Define data
# X = your feature matrix
# y = your target vector

# Create an Extremely Randomized Tree regressor
regressor = ExtraTreesRegressor(n_estimators=100, random_state=0)

# Train the model using the training sets
regressor.fit(X, y)

# Make predictions using the testing set
predicted_values = regressor.predict(X_test)
