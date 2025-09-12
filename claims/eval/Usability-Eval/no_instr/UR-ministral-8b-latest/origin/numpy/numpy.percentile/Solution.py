import numpy as np

def compute_qth_percentile(data, q):
    return np.percentile(data, q, axis=0)

# Example usage:
data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
q = 50
result = compute_qth_percentile(data, q)
print(result)
