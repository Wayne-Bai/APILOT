import numpy as np

def kulsinski_dissimilarity(a, b):
    A = np.sum(a & ~b)
    B = np.sum(~a & b)
    return (A + B) / len(a)

# Example usage
for _ in range(10):
    a = np.random.choice([0, 1], size=10)
    b = np.random.choice([0, 1], size=10)
    print(f"Arrays a: {a} and b: {b}")
    print(f"Kulsinski Dissimilarity: {kulsinski_dissimilarity(a, b)}")
    print("-" * 20)
