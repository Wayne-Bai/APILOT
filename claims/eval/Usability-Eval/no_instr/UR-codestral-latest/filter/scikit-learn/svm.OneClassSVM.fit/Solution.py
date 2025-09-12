from sklearn import svm
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# Generate random classification data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, class_sep=0.8, random_state=0)

# Create a SVM classifier with the RBF (Radial Basis Function) kernel
clf = svm.SVC(kernel='rbf', class_weight='balanced')

# Train the classifier
clf.fit(X, y)

# Create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predict the labels for each point in the mesh
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Reshape the result back to the mesh
Z = Z.reshape(xx.shape)

# Plot the result using matplotlib
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
plt.title('SVM with RBF Kernel')
plt.show()
