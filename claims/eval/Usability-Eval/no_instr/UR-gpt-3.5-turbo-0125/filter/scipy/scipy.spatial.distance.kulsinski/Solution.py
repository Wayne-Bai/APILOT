
import numpy as np

# Define the Kulsinski dissimilarity function
def kulsinski_dissimilarity(u, v):
    n = len(u)
    intersect = np.sum(u & v)
    not_v = np.sum(u & ~v)
    not_u = np.sum(~u & v)
    jaccard = intersect / (intersect + not_v + not_u)
    kul = 1.0 - jaccard * n
    return kul

# Two boolean 1-D arrays
u = np.array([True, False, True, False, True])
v = np.array([True, True, False, False, True])

# Compute the Kulsinski dissimilarity
result = kulsinski_dissimilarity(u, v)
print(result)
