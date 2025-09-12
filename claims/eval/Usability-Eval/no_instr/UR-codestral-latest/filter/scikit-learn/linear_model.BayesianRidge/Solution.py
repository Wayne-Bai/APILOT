from sklearn.linear_model import BayesianRidge
import numpy as np

# Assume we have some data
X = np.array([[-1, 1], [-2, -1], [1, 1], [2, 1]])
Y = np.array([-1, 1, 2, 2])

# Create a BayesianRidge object with default parameters
br = BayesianRidge()

# Use fit method to train the model
br.fit(X, Y)

# Now, the model is trained and can be used to predict new data
# For example:
print(br.predict([[3, 5]]))
