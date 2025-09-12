import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence

# Generate some data
np.random.seed(0)
X = np.random.rand(100, 2)
y = np.sin(2 * np.pi * X[:, 0]) + np.cos(2 * np.pi * X[:, 1])

# Train a model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X, y)

# Plot partial dependence
plot_partial_dependence(model, X, [0, 1], n_jobs=1, response_method='predict')
plt.show()
