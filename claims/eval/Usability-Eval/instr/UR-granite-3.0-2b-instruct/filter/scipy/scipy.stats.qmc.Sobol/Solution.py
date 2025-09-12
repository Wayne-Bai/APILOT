import numpy as np
from scipy.special import sobol_generate

def sobol_engine(dim, num_points):
    # Generate Sobol' sequence
    sobol_sequence = sobol_generate(dim, num_points)

    return sobol_sequence
