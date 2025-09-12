import numpy as np
from scipy.special import kl_div

def jensen_shannon_distance(p, q):
    # Normalize the probability distributions
    p = np.asarray(p) / np.sum(p)
    q = np.asarray(q) / np.sum(q)
    
    # Compute the average probability distribution
    m = 0.5 * (p + q)
    
    # Calculate the Jensen-Shannon divergence
    js_divergence = 0.5 * (kl_div(p, m).sum() + kl_div(q, m).sum())
    
    # Return the square root of the Jensen-Shannon divergence
    return np.sqrt(js_divergence)

# Example usage
p = [0.1, 0.9]
q = [0.5, 0.5]
distance = jensen_shannon_distance(p, q)
print("Jensen-Shannon distance:", distance)
