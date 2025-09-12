import numpy as np
from sklearn.linear_model import ARDRegression
from sklearn.utils import check_array

# Define the data and initialize the model
X = ...  # feature matrix
y = ...  # target vector
ard_model = ARDRegression(n_iter=10)

# Fit the model using the Evidence Maximization algorithm
ard_model.fit(X, y)

# Extract the weights and their estimated precisions
weights = ard_model.coef_
lambda_ = np.diagonal(ard_model.precision_)

# Compute the precision of the noise distribution
alpha = 1 / ard_model.noise_precision_
