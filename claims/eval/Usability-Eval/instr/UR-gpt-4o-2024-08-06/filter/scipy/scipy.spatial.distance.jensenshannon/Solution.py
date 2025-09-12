import numpy as np
from scipy.special import kl_div

def jensen_shannon_distance(p, q):
    # Ensure the inputs are numpy arrays
    p = np.asarray(p, dtype=np.float64)
    q = np.asarray(q, dtype=np.float64)
    
    # Normalize the distributions
    p /= np.sum(p)
    q /= np.sum(q)
    
    # Compute the midpoint
    m = 0.5 * (p + q)
    
    # Compute the Kullback-Leibler divergences
    kl_pm = np.sum(kl_div(p, m))
    kl_qm = np.sum(kl_div(q, m))
    
    # Compute the Jensen-Shannon divergence
    js_divergence = 0.5 * (kl_pm + kl_qm)
    
    # Jensen-Shannon distance is the square root of the divergence
    js_distance = np.sqrt(js_divergence)
    
    return js_distance

# Example usage:
p = [0.2, 0.5, 0.3]
q = [0.1, 0.7, 0.2]
js_distance = jensen_shannon_distance(p, q)
print(f"Jensen-Shannon Distance: {js_distance}")
