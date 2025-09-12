from sklearn.tree import DecisionTreeRegressor

# Create a DecisionTreeRegressor object
dt_reg = DecisionTreeRegressor()

# Assume X is your feature matrix and y is your target variable
# Fit the model to your data
dt_reg.fit(X, y)

# Now you can use the model for predictions
y_pred = dt_reg.predict(X)
