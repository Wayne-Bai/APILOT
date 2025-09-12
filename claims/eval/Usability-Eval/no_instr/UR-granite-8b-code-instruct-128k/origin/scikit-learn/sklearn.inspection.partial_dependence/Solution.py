
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import partial_dependence

# Assume X is your input features and y is your target variable
# X is a numpy array of shape (n_samples, n_features)
# y is a numpy array of shape (n_samples,)

# Create a RandomForestRegressor model
model = RandomForestRegressor()
model.fit(X, y)

# Define the features for which you want to calculate the partial dependence
features = [0, 1]  # Indices of the features

# Calculate the partial dependence
pd_values = partial_dependence(model, X, features)

# Print the partial dependence values
print(pd_values)
