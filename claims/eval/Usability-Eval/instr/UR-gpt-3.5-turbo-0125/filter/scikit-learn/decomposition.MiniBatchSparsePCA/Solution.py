
import numpy as np

def soft_thresholding(x, alpha):
    return np.sign(x) * np.maximum(np.abs(x) - alpha, 0)

def sparse_pca(X, n_components, alpha, max_iter=100, tol=1e-6):
    n_samples, n_features = X.shape
    components = np.random.randn(n_components, n_features)
    
    for _ in range(max_iter):
        prev_components = components.copy()
        
        # Update components
        for i in range(n_components):
            mask = np.ones(n_components, dtype=bool)
            mask[i] = 0
            mean = np.dot(X, components[mask].T)
            components[i] = soft_thresholding(mean, alpha)
        
        # Check for convergence
        if np.linalg.norm(components - prev_components) < tol:
            break
    
    return components

# Usage example
# X is the data matrix, n_components is the desired number of components
# alpha is the sparsity controlling parameter
X = np.random.randn(100, 20)
components = sparse_pca(X, n_components=5, alpha=0.1)
print(components)
