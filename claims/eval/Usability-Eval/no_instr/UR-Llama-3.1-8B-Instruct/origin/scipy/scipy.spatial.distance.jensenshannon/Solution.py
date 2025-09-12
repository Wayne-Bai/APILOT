import numpy as np
from scipy.stats import entropy

def compute_jensen_shannon(p, q):
    """
    Compute the Jensen-Shannon distance (metric) between two probability arrays.

    Parameters:
    p (array): The first probability array.
    q (array): The second probability array.

    Returns:
    distance (float): The Jensen-Shannon distance between the two probability arrays.

    """
    # Compute the entropy of p and q
    entropy_p = entropy(p, base=2)
    entropy_q = entropy(q, base=2)

    # Compute the average entropy of p and q
    avg_entropy = (entropy_p + entropy_q) / 2

    # Compute the Jensen-Shannon divergence
    js_divergence = (entropy(p, q) + entropy(q, p)) / 2

    # Compute the Jensen-Shannon distance
    distance = np.sqrt(js_divergence - avg_entropy)

    return distance

# Example usage:
p = np.array([0.2, 0.3, 0.5])  # First probability array
q = np.array([0.3, 0.3, 0.4])  # Second probability array

distance = compute_jensen_shannon(p, q)
print(f"The Jensen-Shannon distance between the two probability arrays is: {distance}")
