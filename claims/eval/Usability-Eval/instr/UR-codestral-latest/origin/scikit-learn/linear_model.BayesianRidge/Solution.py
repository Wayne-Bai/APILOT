# Import the necessary package
from sklearn.linear_model import BayesianRidge

# Create a sample dataset
# X_train, y_train = get_your_data()

# Create a Bayesian Ridge regressor
reg = BayesianRidge()

# Fit the model to the training data
reg.fit(X_train, y_train)
