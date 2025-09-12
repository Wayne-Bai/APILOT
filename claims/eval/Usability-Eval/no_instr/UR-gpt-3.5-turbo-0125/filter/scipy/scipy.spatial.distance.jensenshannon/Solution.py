
import numpy as np

def jensen_shannon_distance(p, q):
    def jensen_shannon_divergence(p, q):
        m = 0.5 * (p + q)
        return 0.5 * (np.sum(p * np.log2(p/m)) + np.sum(q * np.log2(q/m)))
    
    p = np.array(p)
    q = np.array(q)
    
    m = 0.5 * (p + q)
    return np.sqrt(0.5 * (jensen_shannon_divergence(p, m) + jensen_shannon_divergence(q, m)))

# Example usage
p = [0.3, 0.2, 0.5]
q = [0.1, 0.6, 0.3]
distance = jensen_shannon_distance(p, q)
print('Jensen-Shannon distance:', distance)
