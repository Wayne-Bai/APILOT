import numpy as np

def create_matrix(N, M, k):
    A = np.triu(np.ones((N, M)), k=1-k, dtype=int)
    return A

# Test the function
N, M, k = 5, 5, 2
A = create_matrix(N, M, k)
print(A)
