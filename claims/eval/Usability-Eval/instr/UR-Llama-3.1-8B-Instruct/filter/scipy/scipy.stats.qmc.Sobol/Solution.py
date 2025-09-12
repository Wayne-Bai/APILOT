# Import the necessary libraries from scipy
from scipy.stats import norm
# Import the necessary libraries for generating Sobol sequences
from scipy import spatial

def sobol(n, dim, seed=0):
    """
    Generates a scrambled Sobol' sequence
    Args:
    n (int): The number of points to generate
    dim (int): The number of dimensions to generate for each point
    seed (int): The seed for the random number generator (optional, default=0)
    Returns:
    A 2D numpy array where each row is a point in the Sobol' sequence
    """
    # Initialize the random number generator with the provided seed
    rng = spatial.random.MersenneTwister(seed)
    
    # Generate the scrambled Sobol' sequence
    sobol_seq = spatial.qrng.sobol_spacings(n, dim, rng, scramble=True)
    
    # Return the coherent Sobol sequence
    return spatial.qrng.sobol_space(sobol_seq)

# Example usage
if __name__ == "__main__":
    # Set the parameters for generating the Sobol' sequence
    n_points = 100
    num_dimensions = 2
    
    # Generate the scrambled Sobol' sequence
    sobol_seq = sobol(n_points, num_dimensions)
    
    # Print the generated Sobol' sequence
    print(sobol_seq)
