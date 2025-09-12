from sklearn.datasets import load_iris
from sklearn import datasets
from scipy.sparse import csr_matrix

# load iris dataset as an example
iris = datasets.load_iris()
X = iris.data

# Create a sparse matrix
sparse_matrix = csr_matrix(X)

# Calculate density
density = sparse_matrix.nnz / float(sparse_matrix.shape[0] * sparse_matrix.shape[1])

print("Sparse vector density: ", density)
