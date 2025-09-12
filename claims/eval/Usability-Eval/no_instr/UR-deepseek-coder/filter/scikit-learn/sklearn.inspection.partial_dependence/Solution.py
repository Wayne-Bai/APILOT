import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import PartialDependenceDisplay

# Example dataset
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.rand(100)     # Target variable

# Train a Gradient Boosting Regressor model
model = GradientBoostingRegressor()
model.fit(X, y)

# Calculate partial dependence for the first feature
features = [0]  # Index of the feature to analyze
PartialDependenceDisplay.from_estimator(model, X, features)

# Show the plot
plt.show()
