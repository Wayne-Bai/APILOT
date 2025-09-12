
from sklearn.datasets import make_swiss_roll
from sklearn.manifold import Isomap

X, _ = make_swiss_roll(n_samples=1000, noise=0.2)

# Isomap embedding
isomap = Isomap(n_neighbors=10, n_components=2)
X_projected = isomap.fit_transform(X)

print(X_projected)
