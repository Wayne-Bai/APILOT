import numpy as np
from scipy.sparse import csr_matrix

def create_design_matrix(data, num_features):
    """
    Creates a design matrix from the input data with a specified number of features.

    Parameters:
    data (list of tuples): The input data. Each tuple contains (feature_index, value).
    num_features (int): The number of features in the data.

    Returns:
    csr_matrix: The design matrix in CSR sparse matrix format.
    """
    rows = []
    cols = []
    values = []

    for i, row in enumerate(data):
        for feature_index, value in row:
            rows.append(i)
            cols.append(feature_index)
            values.append(value)

    # Create sparse matrix in Coordinate format
    coo_matrix = np.array((values, (rows, cols)), dtype=np.float)
    
    # Convert to CSR format
    csr_matrix_result = csr_matrix((values, (rows, cols)), shape=(len(data), num_features))

    return csr_matrix_result

# Example usage
data_example = [
    [(0, 1), (2, 3)],
    [(2, 4), (3, 5)]
]
num_features = 5
design_matrix = create_design_matrix(data_example, num_features)

print(design_matrix)
