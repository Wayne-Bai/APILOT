import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Sample data for demonstration
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

y = np.array([0, 1, 0])

# Create a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10)

# Fit the data to the classifier
clf.fit(X, y)

def plot_partial_dependence(estimator, feature_indices, grid_resolution=25, plot=True):
    # Create a grid of values for the selected features
    x_min, x_max = np.min(X[:, feature_indices]), np.max(X[:, feature_indices])
    x = np.linspace(x_min, x_max, grid_resolution)
    grid = np.array([np.array([x]) for _ in range(grid_resolution)])
    grid = np.concatenate([grid, grid[:, -1][:, None].reshape(-1, 1, 1)])

    partial_dependencies = np.array([np.average(estimated_prob[index] == 1, axis=0).mean()
                                     for index in enumerate(np.outer(grid, grid.T))])

    if plot:
        plt.figure(figsize=(6, 6))

        for i in range(len(feature_indices)):
            plt.subplot(1, len(feature_indices), i + 1)
            plt.plot(x, partial_dependencies[feature_indices[i], :], marker="o", linestyle="--")
            plt.xlabel(feature_indices)
            plt.ylabel('Probability')
            plt.grid(True)
        plt.tight_layout()
        plt.show()

# Plot partial dependence for feature 0 and feature 1
plot_partial_dependence(clf, [0, 1])
