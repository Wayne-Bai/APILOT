import scipy

def create_design_matrix(data):
    """
    Returns a design matrix as a CSR format sparse array.

    Parameters:
    data (list): A list of dictionaries, where each dictionary represents a data point and contains the following keys: "feature1", "feature2", "label".

    Returns:
    csr_matrix: A CSR format sparse array representing the design matrix.
    """
    import scipy.sparse as sps

    # Get the number of data points
    num_data_points = len(data)

    # Initialize the design matrix as a sparse array
    design_matrix = sps.csr_matrix((num_data_points, 2))

    # Populate the design matrix with data
    for i, point in enumerate(data):
        design_matrix[i, 0] = point["feature1"]
        design_matrix[i, 1] = point["feature2"]

    return design_matrix
