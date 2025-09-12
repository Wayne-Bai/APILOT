import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample data creation for demonstration
from sklearn.datasets import load_boston
boston = load_boston()
X, y = boston.data, boston.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestRegressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict for the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Feature to explore partial dependence for
feature_index = 5  # Example: selecting the 'RM' feature (index 5) from the Boston dataset

# Create a mesh grid for the feature to plot the partial dependence for
x_grid = np.linspace(X[:, feature_index].min(), X[:, feature_index].max(), 100).reshape(-1, 1)

# Predict on the mesh grid and average the predictions
partial_dependence = model.predict(X_train[:, feature_index].reshape(-1, 1)) + \
                     model.predict(X_test[:, feature_index].reshape(-1, 1))

# Average predictions for each value in the grid
partial_dependence_avg = np.mean(partial_dependence, axis=0)

# Plot the partial dependence
plt.plot(x_grid.squeeze(), partial_dependence_avg)
plt.xlabel(boston.feature_names[feature_index])
plt.ylabel('Average Predicted Value')
plt.title(f'Partial Dependence of {boston.feature_names[feature_index]}')
plt.show()
