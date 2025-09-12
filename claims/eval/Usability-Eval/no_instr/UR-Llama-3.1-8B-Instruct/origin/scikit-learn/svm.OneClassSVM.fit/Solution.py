# Import necessary libraries
from sklearn import svm
import numpy as np
from matplotlib import pyplot as plt

# Let's create a simple dataset
# Training set
X = np.array([[2, 2], [1, 1], [4, 4], [5, 5]])
y = np.array([1, 1, 2, 2])

# Create a kernel ( features mapping )
# Try different kernels ('linear', 'poly', 'rbf','sigmoid',). For our code, we're using 'poly'.
# Create a support vector machine classifier having a RBF kernel
clf = svm.SVC(kernel='poly', gamma='scale', degree=3, C=1, probability=True)

# Train the classifier using the training samples
clf.fit(X, y)

# Predicting the response for test dataset
# Let's predict the response for the input
X_test = np.array([[3, 3], [6, 6]])
y_pred = clf.predict(X_test)

# To visualize the decision boundary, let's plot the decision function
# Create a meshgrid
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Create a contour plot
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y)

# Draw the boundary between the two classes
plt.plot(xx, yy, 'k--')

plt.show()
