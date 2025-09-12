import scipy as sp

# Set the values for N (rows), M (columns), and k (admissible diagonal)
N, M, k = 5, 5, 2

# Create the matrix with ones up to the main diagonal + k
matrix = sp.triu(sp.ones((N, M)), -k)

matrix
