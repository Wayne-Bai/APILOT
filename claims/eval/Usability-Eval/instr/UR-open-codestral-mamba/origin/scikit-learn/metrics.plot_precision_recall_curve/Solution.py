import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.datasets import load_iris

# Load Iris dataset as an example
data = load_iris()
y = data.target != 0  # We'll work on binary classification task, so set y either 0 or 1 based on condition.
X = data.data[:, :2]  # Only take the first two features for simplicity.

# Assume we have plotted the data like the following:
plt.scatter(X[:, 0], X[:, 1], c='b', label='Positive' if y[0] else 'Negative')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.legend()
plt.show()

# Calculate precision-recall pairs for different probability thresholds
precisions, recalls, thresholds = precision_recall_curve(y, X[:, 1])

# Plot Precision-Recall curve
plt.plot(recalls, precisions)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.show()
