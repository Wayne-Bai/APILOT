import scipy.linalg

def zero_above_kth_diagonal(matrix, k):
    return scipy.linalg.triu(matrix, k=k)
