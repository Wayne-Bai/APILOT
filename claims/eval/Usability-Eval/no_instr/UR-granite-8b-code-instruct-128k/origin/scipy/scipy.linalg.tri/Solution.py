import scipy

def construct_matrix(N, M, k):
    A = scipy.zeros((N, M))
    for i in range(N):
        for j in range(M):
            if j <= i + k:
                A[i, j] = 1
    return A
