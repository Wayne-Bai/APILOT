# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn import datasets
import numpy as np

# Load the iris dataset as an example
iris = datasets.load_iris()
X = iris.data

# Create a PCA that will retain 99% of the variance
pca = PCA(n_components=0.99, whiten=True)

# Conduct PCA
data = pca.fit_transform(X)

# Show the shape of the transformed data
print(data.shape)
