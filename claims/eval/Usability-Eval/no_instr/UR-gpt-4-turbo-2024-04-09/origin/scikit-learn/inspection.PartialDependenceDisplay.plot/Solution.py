import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.model_selection import train_test_split

# Load data
boston = load_boston()
X, y = boston.data, boston.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Build the model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=0)
model.fit(X_train, y_train)

# Feature names
features = [5, 12]  # Example features: RM and LSTAT from Boston dataset

# Plot partial dependence plots
fig, ax = plt.subplots(figsize=(10, 6))
plot_partial_dependence(model, X_train, features, feature_names=boston.feature_names, ax=ax)
plt.suptitle("Partial Dependence Plots")
plt.subplots_adjust(top=0.9)
plt.show()
