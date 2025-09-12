from scipy import stats
import numpy as np

def jensen_shannon_distance(p1, p2):
    """
    Compute the Jensen-Shannon distance (metric) between two probability arrays.

    The Jensen-Shannon distance is defined as the square root of the Jensen-Shannon
    divergence, which itself is defined as the average entropy of the two
    probability distributions minus the entropy of their convex combination.

    Parameters:
    p1 (array_like): The first probability distribution. Must sum up to 1.
    p2 (array_like): The second probability distribution. Must sum up to 1.

    Returns:
    js_distance (float): The Jensen-Shannon distance between two distributions.

    Raises:
    ValueError: If the input arrays do not sum up to 1.
    """
    # Check if inputs are valid probability distributions
    if not np.allclose(np.sum(p1, axis=0), 1):
        raise ValueError("Input arrays must sum up to 1.")
    if not np.allclose(np.sum(p2, axis=0), 1):
        raise ValueError("Input arrays must sum up to 1.")

    # Compute the convex combination of the two distributions
    m = 0.5 * (p1 + p2)

    # Compute the entropy of each distribution
    avg_entropy = 0.5 * (stats.entropy(p1, base=2) + stats.entropy(p2, base=2))

    # Compute the entropy of the convex combination
    m_entropy = stats.entropy(m, base=2)

    # Compute the Jensen-Shannon divergence
    js_divergence = avg_entropy - m_entropy

    # Compute the Jensen-Shannon distance
    js_distance = np.sqrt(js_divergence)

    return js_distance

# Example usage
p1 = np.array([0.2, 0.3, 0.5])
p2 = np.array([0.4, 0.3, 0.3])

js_distance = jensen_shannon_distance(p1, p2)
print("Jensen-Shannon distance:", js_distance)
