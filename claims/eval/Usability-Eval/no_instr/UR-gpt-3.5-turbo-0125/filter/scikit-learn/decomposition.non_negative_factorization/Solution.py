
import numpy as np

def NMF(X, n_components=5, max_iter=200, tol=1e-4):
    def cost_function(V, W, H):
        return np.linalg.norm(V - np.dot(W, H))
    
    def update_W(V, W, H):
        WHt = np.dot(W, H.T)
        WHt[WHt == 0] = np.finfo(float).eps
        return W * np.dot(V / WHt, H.T)

    def update_H(V, W, H):
        WHt = np.dot(W, H.T)
        WHt[WHt == 0] = np.finfo(float).eps
        return H * np.dot(W.T, V / WHt)
    
    V = X
    m, n = V.shape
    W = np.abs(np.random.randn(m, n_components))
    H = np.abs(np.random.randn(n_components, n))
    
    for i in range(max_iter):
        W_new = update_W(V, W, H)
        H_new = update_H(V, W, H)
        
        cost = cost_function(V, W_new, H_new)
        
        if np.abs(cost - cost_function(V, W, H)) < tol:
            break
        
        W, H = W_new, H_new
        
    return W, H

X = np.random.rand(100, 50)
W, H = NMF(X, n_components=10, max_iter=200, tol=1e-4)
