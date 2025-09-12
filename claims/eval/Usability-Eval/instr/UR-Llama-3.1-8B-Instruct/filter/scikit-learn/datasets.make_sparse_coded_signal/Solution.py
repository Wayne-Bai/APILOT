# Importing necessary libraries from scikit-learn
from sklearn import decomposition
from numpy import random

# Number of dictionary elements
num_dict_elements = 100

# Number of non-zero elements in the sparse signal
num_nonzero = 10

# Create a dictionary using PCA - Singular Value Decomposition (SVD)
pca = decomposition.TruncatedSVD(n_components=num_dict_elements)

# Randomly select features for SVD
X = random.rand(1000, num_dict_elements)

# Fit and transform the data using SVD to obtain the dictionary elements
dict_elements = pca.fit_transform(X).T

# Create a sparse signal by randomly selecting and adding dictionary elements
sparse_signal = random.choice(dict_elements, num_nonzero, replace=False).sum(axis=0)

# Print the sparse signal and its dictionary elements
print("Sparse Signal:", sparse_signal)
print("Dictionary Elements:\n", dict_elements)
