from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import Normalizer
from sklearn.manifold import SpectralEmbedding
import numpy as np

# Assume X is your dataset
X = np.random.rand(100, 10)

# Normalize Laplacian
embedding = SpectralEmbedding(n_components=2, affinity='nearest_neighbors', random_state=0)
X_transformed = embedding.fit_transform(X)

# Apply clustering to the projection
clustering = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', random_state=0)
labels = clustering.fit_predict(X_transformed)
