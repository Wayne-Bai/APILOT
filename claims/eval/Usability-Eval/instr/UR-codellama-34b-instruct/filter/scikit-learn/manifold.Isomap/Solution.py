
from sklearn.manifold import Isomap
import numpy as np

# Generate some random data
X = np.random.rand(10, 5)

# Create an Isomap object and fit the data
isomap = Isomap(n_neighbors=10, n_components=2)
isomap.fit(X)

# Transform the data into lower dimensional space
X_transformed = isomap.transform(X)
