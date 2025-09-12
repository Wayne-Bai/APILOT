import numpy as np
from scipy.spatial.distance import jensenshannon

def jensen_shannon_distance(p, q):
    """
    Compute the Jensen-Shannon distance between two probability distributions.
    
    Parameters:
    p (array-like): First probability distribution.
    q (array-like): Second probability distribution.
    
    Returns:
    float: The Jensen-Shannon distance.
    """
    # Ensure the two distributions sum to 1
    p = np.array(p)
    q = np.array(q)
    p /= p.sum()
    q /= q.sum()
    
    # Calculate the Jensen-Shannon distance using scipy's jensenshannon function
    distance = jensenshannon(p, q)
    return distance

# Example usage:
p = [0.1, 0.9]
q = [0.8, 0.2]
distance = jensen_shannon_distance(p, q)
print(f"Jensen-Shannon Distance: {distance}")
