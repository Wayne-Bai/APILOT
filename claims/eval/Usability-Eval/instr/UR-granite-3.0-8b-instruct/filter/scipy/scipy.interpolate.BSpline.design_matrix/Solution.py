from scipy.sparse import csr_matrix

def create_design_matrix(data):
    # Assuming data is a dictionary with keys 'X' and 'y'
    X = data['X']
    y = data['y']

    # Convert X to CSR format
    X_csr = csr_matrix(X)

    return X_csr, y
