from scipy.spatial.distance import euclidean

def kulsinski_dissimilarity(x, y):
    n = len(x)
    if n == 0:
        return 0
    else:
        return euclidean(x, y) / (n - 1)
