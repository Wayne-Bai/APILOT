from scipy.spatial.distance import jensenshannon

def compute_jensen_shannon_distance(p, q):
    return jensenshannon(p, q)

# Example usage:
p = [0.1, 0.2, 0.3, 0.4]
q = [0.2, 0.3, 0.4, 0.1]
distance = compute_jensen_shannon_distance(p, q)
print(f"The Jensen-Shannon distance is: {distance}")
