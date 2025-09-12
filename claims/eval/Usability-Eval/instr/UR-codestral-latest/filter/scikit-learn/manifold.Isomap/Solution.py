from sklearn.manifold import Isomap
import numpy as np

# Let's assume we have a 2D dataset for simplicity
X = np.random.rand(100, 2)

# We will embed it into 2 dimensions
isomap = Isomap(n_components=2)
X_transformed = isomap.fit_transform(X)
