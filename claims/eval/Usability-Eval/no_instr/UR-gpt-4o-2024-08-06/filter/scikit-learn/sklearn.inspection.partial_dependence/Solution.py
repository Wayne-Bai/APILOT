import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_friedman1
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import partial_dependence
from sklearn.inspection import PartialDependenceDisplay
from sklearn.model_selection import train_test_split

# Generate a synthetic dataset
X, y = make_friedman1(n_samples=1000, n_features=10, random_state=0)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Gradient Boosting model
estimator = GradientBoostingRegressor()
estimator.fit(X_train, y_train)

# Define the features for which you want to plot partial dependence
features_to_plot = [0, 1, (0, 1)]

# Calculate and plot the partial dependence
fig, ax = plt.subplots(figsize=(10, 6))
display = PartialDependenceDisplay.from_estimator(estimator, X_train, features_to_plot, ax=ax)

# Show the plot
plt.suptitle('Partial Dependence Plots')
plt.subplots_adjust(top=0.9)  # Adjust title position
plt.show()
