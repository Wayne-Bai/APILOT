from sklearn.tree import DecisionTreeRegressor

# Assuming X is your feature set and y is your target variable
# X = ...
# y = ...

# Initialize the DecisionTreeRegressor
dt_regressor = DecisionTreeRegressor()

# Fit the model to the data
dt_regressor.fit(X, y)
