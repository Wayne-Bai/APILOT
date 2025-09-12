# Required Python code using scikit-learn for building a decision tree regressor
from sklearn.tree import DecisionTreeRegressor

# Assume X and y are your features and target dataset respectively
# X = your_features
# y = your_target

# Creating the decision tree regressor model
regressor = DecisionTreeRegressor()

# Training the model with the dataset
regressor.fit(X, y)
