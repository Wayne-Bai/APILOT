from sklearn.utils.sparsefuncs import min_max_axis

def compute_density(sparse_vector):
    """
    Compute the density of a sparse vector.

    Parameters:
    sparse_vector (scipy.sparse matrix): The sparse vector.

    Returns:
    float: The density of the sparse vector.
    """
    # Compute the minimum and maximum values along the axis
    min_val, max_val = min_max_axis(sparse_vector, axis=0)

    # Compute the range of the sparse vector
    range_val = max_val - min_val

    # Compute the density of the sparse vector
    density = (sparse_vector.nnz / len(sparse_vector)) * (range_val / (max_val - min_val))

    return density
