from scipy.spatial import distance
import numpy as np

def jensen_shannon_distance(P, Q):
    '''
    Computes the Jensen-Shannon distance (metric) between two probability arrays.
    This is the square root of the Jensen-Shannon divergence.

    Parameters:
    P (array-like): first probability array
    Q (array-like): second probability array

    Returns:
    distance (float): Jensen-Shannon distance between P and Q
    '''
    P = np.array(P)
    Q = np.array(Q)
    if len(P) != len(Q):
        raise ValueError("Probability arrays must have the same length.")
    if (np.any(P < 0) or np.any(Q < 0)) or (np.any(P > 1) or np.any(Q > 1)):
        raise ValueError("Probability arrays must be between 0 and 1.")
    M = 0.5 * (P + Q)
    JSD = 0.5 * (distance.kl_divergence(P, M) + distance.kl_divergence(Q, M))
    distance = np.sqrt(JSD)

    return distance
