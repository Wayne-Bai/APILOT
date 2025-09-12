import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import PartialDependenceDisplay
from sklearn.model_selection import train_test_split

# Load the dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# List of features for which to generate partial dependence plots
feature_indices = [0, 1, 2, 3, 4, 5, 6, 7]  # indices of chosen features

# Generate partial dependence plot
display = PartialDependenceDisplay.from_estimator(
    model,
    X_test,
    features=feature_indices,
    grid_resolution=50
)

plt.show()
