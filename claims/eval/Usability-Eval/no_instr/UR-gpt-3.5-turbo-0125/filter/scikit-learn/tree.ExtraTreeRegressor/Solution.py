
# Importing the necessary libraries
from sklearn.ensemble import ExtraTreesRegressor

# Creating an Extremely Randomized Trees Regressor model
extra_trees_regressor = ExtraTreesRegressor()

# Training the model with training data
extra_trees_regressor.fit(X_train, y_train)

# Making predictions
predictions = extra_trees_regressor.predict(X_test)
