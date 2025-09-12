
import numpy as np
import random

def random_state(seed):
    """
    Generate a numpy.random.RandomState instance using the specified seed.
    
    Args:
        seed (int): The seed to use for generating the RandomState instance.
        
    Returns:
        numpy.random.RandomState: The generated RandomState instance.
    """
    return np.random.RandomState(seed)
