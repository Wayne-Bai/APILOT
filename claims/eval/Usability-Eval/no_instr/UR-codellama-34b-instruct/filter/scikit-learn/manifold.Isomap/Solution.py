
from sklearn.manifold import Isomap
import numpy as np

# Generate some sample data
n_samples = 100
data = np.random.rand(n_samples, 3)

# Create an Isomap embedding object
isomap = Isomap(n_neighbors=5)

# Fit the Isomap embedding to the data
isomap.fit(data)

# Transform the data into the lower-dimensional space
X_iso = isomap.transform(data)
