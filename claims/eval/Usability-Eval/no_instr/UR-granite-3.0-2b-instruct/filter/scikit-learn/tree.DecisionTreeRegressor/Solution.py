from sklearn.tree import DecisionTreeRegressor

# Assuming X is your features and y is your target variable
# X = ...
# y = ...

# Initialize the decision tree regressor
dt_reg = DecisionTreeRegressor()

# Fit the model with your data
dt_reg.fit(X, y)

# Now you can use the model to make predictions
# For example, to predict the target variable for a new input
# new_input = ...
# prediction = dt_reg.predict(new_input)
