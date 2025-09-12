from sklearn import neighbors
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
X = np.random.rand(100, 2)  # 100 samples with 2 features
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Labels based on a simple rule

# Fit a KNeighborsClassifier
clf = neighbors.KNeighborsClassifier(n_neighbors=5)
clf.fit(X, y)

# Create a mesh to plot the decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# Predict the decision boundary
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the results
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
plt.title("Soft Boundary Detection with KNeighborsClassifier")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
