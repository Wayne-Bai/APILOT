# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn import datasets

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Show shape of original and reduced data
print(f'Original shape: {X.shape}, reduced shape: {X_pca.shape}')
