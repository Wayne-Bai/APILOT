import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence

# Generate some data
rng = np.random.RandomState(1)
X = rng.rand(100, 1)
y = np.sin(2 * np.pi * X).ravel()

# Create a RandomForestRegressor
clf = RandomForestRegressor(random_state=0)
clf.fit(X, y)

# Plot partial dependence plot
fig, ax = plt.subplots(figsize=(8, 6))
plot_partial_dependence(clf, X, [0], response_method='predict', n_jobs=1, ax=ax)
plt.show()
