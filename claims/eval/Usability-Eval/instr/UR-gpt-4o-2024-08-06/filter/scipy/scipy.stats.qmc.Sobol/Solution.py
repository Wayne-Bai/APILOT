import numpy as np
import scipy.stats

def generate_sobol_sequence(dimensions, num_points, seed=None):
    """
    Generate a Sobol sequence with the given number of dimensions and points.

    :param dimensions: Number of dimensions
    :param num_points: Number of points to generate
    :param seed: Random seed for reproducibility (optional)
    :return: NumPy array of Sobol sequence
    """
    
    # Creating a Sobol sequence generator
    sobol = scipy.stats.qmc.Sobol(d=dimensions, scramble=True, seed=seed)
    
    # Generating Sobol points
    sobol_points = sobol.random_base2(m=int(np.log2(num_points)))
    
    return sobol_points

# Example usage
dimensions = 3
num_points = 8  # needs to be a power of 2 for Sobol sequences with the specified method
sobol_sequence = generate_sobol_sequence(dimensions, num_points)

print(sobol_sequence)
