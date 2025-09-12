from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import partial_dependence
import numpy as np
import matplotlib.pyplot as plt

# Assuming that X is the feature matrix and y is the target variable
model = GradientBoostingRegressor()
model.fit(X, y)

# Calculate partial dependence for feature 0 and feature 1
features = [0, 1]
pdp, axes = partial_dependence(model, X, features)

# Plot partial dependence plot
fig, ax = plt.subplots(figsize=(8, 8))
for i in range(len(features)):
    ax.plot(axes[i], pdp[i], label='PDP (feature {})'.format(features[i]))
ax.set_xlabel('Feature value')
ax.set_ylabel('Partial dependence')
ax.grid(True)
plt.legend()
plt.show()
