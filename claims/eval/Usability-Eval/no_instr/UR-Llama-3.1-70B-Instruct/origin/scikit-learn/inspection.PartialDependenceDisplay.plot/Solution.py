# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import partial_dependence, PartialDependenceDisplay
from sklearn.inspection import plot_partial_dependence

# Creating a sample dataset
np.random.seed(0)
n_samples = 1000
n_features = 10
X = np.random.randn(n_samples, n_features)
y = 3 * X[:, 0] + 2 * np.sin(np.pi * X[:, 1])

# Fitting a random forest model to the data
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X, y)

# Generating partial dependence plots
fig, axs = plt.subplots(figsize=(12, 8))
plot_partial_dependence(rf, X, ['feature_0', 'feature_1'], 
                        feature_names=['Feature 0', 'Feature 1'], n_cols=2, ax=axs)

plt.tight_layout()
plt.show()
