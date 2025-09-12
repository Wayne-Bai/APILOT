
import numpy as np

def partial_least_squares(X, y, n_components):
    n = X.shape[0]
    p = X.shape[1]
    
    W = np.zeros((p, n_components))
    T = np.zeros((n, n_components))
    P = np.zeros((p, n_components))
    Q = np.zeros((1, n_components))
    
    for i in range(n_components):
        t = X.dot(y.T) / np.linalg.norm(X.dot(y.T))
        w = X.T.dot(t) / np.linalg.norm(X.T.dot(t))
        p = X.T.dot(t) / np.linalg.norm(X.T.dot(t))
        q = (t.T.dot(y)) / np.linalg.norm(t.T.dot(y))
        
        T[:, i] = t.flatten()
        W[:, i] = w.flatten()
        P[:, i] = p.flatten()
        Q[0, i] = q
    
        X = X - np.outer(t, p.T)
        y = y - np.outer(t, q.T)
    
    return T, W, P, Q

# Example usage
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([[0.1], [0.2], [0.3], [0.4]])
n_components = 2

T, W, P, Q = partial_least_squares(X, y, n_components)

print("T:", T)
print("W:", W)
print("P:", P)
print("Q:", Q)
