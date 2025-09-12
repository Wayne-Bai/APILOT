from sklearn.tree import DecisionTreeRegressor

# Assuming we have our data
# X - feature matrix
# y - target variable

# Create a decision tree regressor
regressor = DecisionTreeRegressor()

# Fit the data to our model
regressor.fit(X, y)
