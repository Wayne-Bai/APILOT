from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load an example dataset
iris = load_iris()
X = iris.data  # we only take the first two features for simplicity

# Initialize PCA
pca = PCA(n_components=2)

# Fit the model with X and apply the dimensionality reduction on X
X_r = pca.fit_transform(X)

# Plot the explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)

# Visualize the PCA result
plt.figure()
for color, i, target_name in zip(['navy', 'turquoise', 'darkorange'], [0, 1, 2], iris.target_names):
    plt.scatter(X_r[iris.target == i, 0], X_r[iris.target == i, 1], color=color, alpha=.8, lw=2,
                label=target_name)

plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
