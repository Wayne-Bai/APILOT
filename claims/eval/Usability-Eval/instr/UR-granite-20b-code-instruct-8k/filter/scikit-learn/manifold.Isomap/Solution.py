from sklearn.manifold import Isomap
import numpy as np

# Generate some random data
data = np.random.rand(100, 3)

# Create an instance of the Isomap class
iso = Isomap(n_components=2)

# Fit the data to the Isomap model
iso.fit(data)

# Transform the data to the isometric embedding
embedded_data = iso.transform(data)

print(embedded_data)
