import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import PartialDependenceDisplay
import matplotlib.pyplot as plt

# Example dataset
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.rand(100)     # Target variable

# Train a GradientBoostingRegressor model
model = GradientBoostingRegressor()
model.fit(X, y)

# Calculate partial dependence for the first feature
features = [0]  # Index of the feature to analyze
display = PartialDependenceDisplay.from_estimator(model, X, features)

# Plot the partial dependence
display.plot()
plt.show()
