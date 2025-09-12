import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import plot_partial_dependence
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load iris dataset as an example
iris = load_iris()
X, y = iris.data, iris.target

# Create a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the classifier on the data
clf.fit(X, y)

# Define the features to plot partial dependence for
features = [0, (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]

# Plot partial dependence for the features
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for i, feat in enumerate(features):
    ax = axs[i//3, i%3]
    plot_partial_dependence(clf, X, features=feat, response_method='auto', n_jobs=1, ax=ax)
    ax.set_title(f'Feature {feat}')

plt.tight_layout()
plt.show()
