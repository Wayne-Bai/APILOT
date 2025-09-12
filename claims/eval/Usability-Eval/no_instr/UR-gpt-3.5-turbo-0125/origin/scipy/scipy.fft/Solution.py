
import numpy as np

def discrete_fourier_transform(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    
    return X

# Example usage:
x = np.array([0, 1, 2, 3])
X = discrete_fourier_transform(x)
print(X)
