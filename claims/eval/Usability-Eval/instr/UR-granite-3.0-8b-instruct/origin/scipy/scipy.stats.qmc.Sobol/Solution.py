import numpy as np
from scipy.spatial import Sobol

def generate_sobol_sequence(dim, n):
    """
    Generate a Sobol sequence of length n in dimension dim.

    Parameters:
    dim (int): The number of dimensions.
    n (int): The number of samples to generate.

    Returns:
    numpy.ndarray: A (n x dim) array containing the Sobol sequence.
    """
    sobol_engine = Sobol(dim, scramble=True)
    return sobol_engine.random(n)
