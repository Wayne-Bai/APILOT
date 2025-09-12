from sklearn.utils import sparsefuncs

def compute_density(sparse_vector):
    return sparsefuncs.sparse_density(sparse_vector)
