import matplotlib.pyplot as plt
from sklearn.inspection import PartialDependenceDisplay
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston

# Load data
X, y = load_boston(return_X_y=True)

# Train model
model = GradientBoostingRegressor()
model.fit(X, y)

# Plot partial dependence
features = [0, (0, 1)]
PartialDependenceDisplay.from_estimator(model, X, features=features)
plt.show()
