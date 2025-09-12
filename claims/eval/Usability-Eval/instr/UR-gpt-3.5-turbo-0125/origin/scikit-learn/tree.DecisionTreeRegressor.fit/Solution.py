
from sklearn.tree import DecisionTreeRegressor

# Assuming X and y are the training set
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]

# Create decision tree regressor model
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

# Now you can use the regressor for prediction or evaluation
