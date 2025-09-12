from sklearn.decomposition import IncrementalPCA
import numpy as np

# Your data here
data = np.array([...])

# Example usage
pca = IncrementalPCA(n_components=10)
pca.fit(data)

print(pca.coef_)

# You can extract the explained variance as well with:
explained_variance = pca.explained_variance_
