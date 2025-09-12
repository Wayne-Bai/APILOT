# import necessary libraries
import numpy as np
from sklearn.manifold import Isomap
from sklearn import datasets

# load the iris dataset
iris = datasets.load_iris()
X = iris.data

# apply Isomap embedding to the iris data
n_components = 2
iso = Isomap(n_components=n_components)
X_transformed = iso.fit_transform(X)

# print the transformed data
print(X_transformed)
