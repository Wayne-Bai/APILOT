
from sklearn.decomposition import PCA
import numpy as np
# Assuming X is the input data with shape (n_samples, n_features)
X = np.random.rand(100, 10)
pca = PCA(n_components=2)
X_transformed = pca.fit_transform(X)
