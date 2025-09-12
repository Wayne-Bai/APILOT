import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_friedman1
from sklearn.inspection import plot_partial_dependence

# Create some sample data
X, y = make_friedman1(n_samples=500, n_features=10, random_state=0)

# Fit a gradient boosting model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0)
model.fit(X, y)

# Plot partial dependence
features = [0, 1, (0, 1)]
plot_partial_dependence(model, X, features) 
plt.suptitle('Partial dependence of features 1, 2 and interaction between 1 and 2')
plt.subplots_adjust(top=0.9)  # Adjust the title to be visible
plt.show()
