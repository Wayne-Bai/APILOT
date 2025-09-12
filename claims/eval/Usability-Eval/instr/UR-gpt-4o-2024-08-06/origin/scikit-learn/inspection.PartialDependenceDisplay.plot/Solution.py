import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_friedman1
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import PartialDependenceDisplay
from sklearn.model_selection import train_test_split

# Generate some data
X, y = make_friedman1(n_samples=500, noise=0.1, random_state=0)

# Split the data into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train a regression model
model = GradientBoostingRegressor(random_state=0)
model.fit(X_train, y_train)

# Define the features for which we want to plot partial dependence
features = [0, 1, 2]  # You can specify the features for which you want to create the plots

# Create a partial dependence plot
PartialDependenceDisplay.from_estimator(model, X_test, features)
plt.show()
