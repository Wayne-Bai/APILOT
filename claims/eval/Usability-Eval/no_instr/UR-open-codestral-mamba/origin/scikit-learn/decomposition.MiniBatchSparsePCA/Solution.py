from sklearn import datasets
from sklearn.decomposition import SparsePCA
from sklearn.preprocessing import StandardScaler

# Load data
iris = datasets.load_iris()
X = iris.data

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Apply SparsePCA
sparse_pca = SparsePCA(n_components=2, alpha=0.1, ridge_alpha=0.01)
X_sparse = sparse_pca.fit_transform(X)

# you can now use X_sparse for further analysis
