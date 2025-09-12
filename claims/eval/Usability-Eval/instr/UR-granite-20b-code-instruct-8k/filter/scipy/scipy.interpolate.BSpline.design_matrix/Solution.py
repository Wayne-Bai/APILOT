import numpy as np
import scipy.sparse as sps

def design_matrix(data):
    """
    This function returns a design matrix as a CSR format sparse array.

    Parameters
    ----------
    data : array_like
        Input data.

    Returns
    -------
    design_matrix : scipy.sparse.csr.csr_matrix
        Design matrix in CSR format.
    """
    design_matrix = sps.csr_matrix(data)
    return design_matrix
