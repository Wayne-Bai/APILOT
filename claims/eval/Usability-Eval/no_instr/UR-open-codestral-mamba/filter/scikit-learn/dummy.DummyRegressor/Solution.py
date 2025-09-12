from sklearn.tree import DecisionTreeRegressor

# Define the model
model = DecisionTreeRegressor(max_depth = 1)

# your features and targets should be defined
#X, y = your_features, your_targets

# Fit the model to your data
model.fit(X, y)
