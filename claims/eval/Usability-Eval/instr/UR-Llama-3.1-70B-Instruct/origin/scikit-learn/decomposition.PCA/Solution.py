# Importing necessary libraries
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Generating a random dataset
np.random.seed(0)
X = np.random.rand(100, 10)

# Standardizing features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Applying PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)

# Explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)

# Plotting the results
plt.figure(figsize=(10, 8))
plt.scatter(X_pca[:, 0], X_pca[:, 1], s=20, c='b', alpha=0.5)
plt.title("Principal Component Analysis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
