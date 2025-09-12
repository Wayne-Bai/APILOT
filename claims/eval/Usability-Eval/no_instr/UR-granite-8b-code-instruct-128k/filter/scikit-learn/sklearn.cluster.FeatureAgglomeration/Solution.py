from sklearn.cluster import AgglomerateFeatures
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Generate a random binary classification problem
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, random_state=42)

# Apply PCA to reduce the dimensionality of the feature space
pca = PCA(n_components=5)
X_pca = pca.fit_transform(X)

# Create an AgglomerateFeatures transformer
af = AgglomerateFeatures(n_clusters=None)

# Fit the transformer to the PCA-transformed data
X_transformed = af.fit_transform(X_pca)

# Visualize the clustering results using a scatter plot
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.show()
