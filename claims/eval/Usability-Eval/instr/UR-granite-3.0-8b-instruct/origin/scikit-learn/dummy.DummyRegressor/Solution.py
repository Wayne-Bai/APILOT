from sklearn.linear_model import LinearRegression

# Assuming X is your feature matrix and y is your target variable
X = ...
y = ...

# Create a Linear Regression object
regressor = LinearRegression()

# Train the model using the training sets
regressor.fit(X, y)

# Make predictions using the testing set
y_pred = regressor.predict(X)
