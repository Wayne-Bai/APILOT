import numpy as np
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix

# Generate a random dictionary and data matrix
np.random.seed(0)
num_items = 100
num_features = 20
data = np.random.rand(num_items, num_features)

# Convert data to a sparse matrix
data_sparse = csr_matrix(data)

# Apply Truncated SVD for matrix factorization
svd = TruncatedSVD(n_components=5, random_state=0)
U = svd.fit_transform(data_sparse)

# Calculate V
V = svd.components_.T

print("User-Item Factor Matrix (U):\n", U)
print("Item-Feature Factor Matrix (V):\n", V)
