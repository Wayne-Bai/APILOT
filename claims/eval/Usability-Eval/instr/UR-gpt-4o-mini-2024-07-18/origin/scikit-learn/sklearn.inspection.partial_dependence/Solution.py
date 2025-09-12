import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# Load dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Plot partial dependence
features = [0, 1, 2]  # Specify the features to plot
plt.figure(figsize=(12, 8))
plot_partial_dependence(model, X_train, features, kind='both', n_jobs=-1)
plt.show()
