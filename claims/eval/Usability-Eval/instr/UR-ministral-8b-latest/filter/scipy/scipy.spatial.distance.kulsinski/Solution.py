import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.stats import binom

def kulsinski_dissimilarity(array1, array2):
    common = np.sum(array1 == array2)
    diff = np.min([np.sum(array1), np.sum(array2)])
    return 1 / (1 + common / diff)

def kulsinski_dissimilarity_matrix(data):
    dists = pdist(data, metric=kulsinski_dissimilarity)
    return squareform(dists)

array1 = np.array([True, False, True, False, True])
array2 = np.array([False, True, True, False, True])

matrix = kulsinski_dissimilarity_matrix([array1, array2])
print(matrix)
