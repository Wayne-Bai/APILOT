from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
X = np.random.randn(100, 2)

# Create a soft boundary using Support Vector Classification
clf = SVC(kernel='rbf', C=1.0, gamma='scale')  # C is the regularization parameter, gamma is for RBF kernel
clf.fit(X, np.zeros(len(X)))  # Using zeros as labels since we're just interested in the boundary

# Plotting the samples
plt.scatter(X[:, 0], X[:, 1], c='b', s=30)

# Create a mesh to plot the decision boundary
xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision function (boundary)
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='r')
plt.title("Soft Boundary of the Set of Samples X")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
