from scipy import sparse

def calculate_density(sparse_vector):
    # Count the number of non-zero elements in the sparse vector
    non_zero_elements = sparse_vector.count_nonzero()

    # The total number of elements in the sparse vector is the size of the vector
    total_elements = sparse_vector.shape[0]

    # Density is the ratio of non-zero elements to total elements
    density = non_zero_elements / total_elements

    return density
