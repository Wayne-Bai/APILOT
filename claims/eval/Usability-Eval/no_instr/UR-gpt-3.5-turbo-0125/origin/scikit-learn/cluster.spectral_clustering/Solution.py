
from sklearn.cluster import SpectralClustering
from sklearn.manifold import SpectralEmbedding
from sklearn.preprocessing import Normalizer
from sklearn.datasets import make_moons

# Create a dataset
X, _ = make_moons(n_samples=100, noise=0.1, random_state=42)

# Normalizing the data
normalizer = Normalizer()
X_norm = normalizer.fit_transform(X)

# Finding the spectral embedding
spectral_embedding = SpectralEmbedding(n_components=2)
X_se = spectral_embedding.fit_transform(X_norm)

# Applying clustering to the projection of the normalized Laplacian
spectral_clustering = SpectralClustering(n_clusters=2, random_state=42)
spectral_clustering.fit(X_se)
