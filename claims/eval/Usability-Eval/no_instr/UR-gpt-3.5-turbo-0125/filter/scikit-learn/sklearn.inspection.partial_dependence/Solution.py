
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# Create a random dataset
X, y = make_regression(n_samples=1000, n_features=5, noise=0.1)

# Train a Random Forest Regressor model
model = RandomForestRegressor()
model.fit(X, y)

# Plot the partial dependence of features
features = [(0, 1), (2, 3)]  # Pair of features for which partial dependence is to be plotted
plot_partial_dependence(model, X, features, n_cols=2, grid_resolution=50)
plt.suptitle('Partial Dependence of Features')
plt.show()
