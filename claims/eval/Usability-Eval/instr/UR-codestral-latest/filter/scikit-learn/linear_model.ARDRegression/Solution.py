from sklearn.linear_model import BayesianRidge
import numpy as np

# Assume X is your feature matrix and y is your target variable
# X = np.array([...])
# y = np.array([...])

# Create an instance of BayesianRidge
reg = BayesianRidge()

# Fit the model
reg.fit(X, y)

# To predict new values
# predictions = reg.predict(X_new)
