from sklearn.manifold import Isomap
from sklearn.datasets import make_swiss_roll
import numpy as np

# Generate Swiss roll dataset
X, _ = make_swiss_roll(n_samples=1000, noise=0.1)

# Initialize Isomap with 2 components
iso = Isomap(n_components=2, random_state=42)

# Fit the model to the data
X_2d = iso.fit_transform(X)

# Print the embedded data
print(X_2d)
