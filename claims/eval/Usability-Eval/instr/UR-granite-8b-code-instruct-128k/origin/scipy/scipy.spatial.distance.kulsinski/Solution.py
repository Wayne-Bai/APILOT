from scipy.spatial import distance
import numpy as np

def compute_kulsinski_dissimilarity(u, v):
    dissimilarity = distance.kulsinski(u, v)
    return dissimilarity

u = np.array([True, False, True, False, True])
v = np.array([False, True, True, False, True])

print(compute_kulsinski_dissimilarity(u, v))
