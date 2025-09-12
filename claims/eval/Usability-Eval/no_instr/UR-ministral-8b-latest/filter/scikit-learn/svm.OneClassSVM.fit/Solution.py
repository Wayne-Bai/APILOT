# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix

# Generating a synthetic dataset
X, y = make_moons(n_samples=500, noise=0.1)

# Setting the parameters
clf = IsolationForest(contamination=0.1)

# Fitting the model
clf.fit(X)

# Predicting the anomaly scores
y_pred = clf.decision_function(X)

# Plotting the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap=plt.cm.Paired, edgecolor='k', s=20)
plt.title('Isolation Forest Soft Boundary Detection')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
