from sklearn.manifold import Isomap
from sklearn.datasets import load_digits

# Load sample data
X, _ = load_digits(return_X_y=True)

# Create an Isomap instance with 2 components
isomap = Isomap(n_components=2)

# Fit and transform the data
X_transformed = isomap.fit_transform(X)
