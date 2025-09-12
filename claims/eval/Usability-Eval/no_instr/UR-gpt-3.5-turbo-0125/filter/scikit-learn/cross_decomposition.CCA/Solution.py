
import numpy as np

def canonical_correlation_analysis(X, Y):
    n = X.shape[0]
    m = Y.shape[0]
    
    X_tilde = X - np.mean(X, axis=0)
    Y_tilde = Y - np.mean(Y, axis=0)
    
    S_x = (1/(n-1)) * np.dot(X_tilde.T, X_tilde)
    S_y = (1/(m-1)) * np.dot(Y_tilde.T, Y_tilde)
    
    S_xy = (1/(n-1)) * np.dot(X_tilde.T, Y_tilde)
    
    U_x, _, _ = np.linalg.svd(S_x)
    U_y, _, _ = np.linalg.svd(S_y)
    
    C_xx = np.linalg.inv(np.sqrt(np.diag(np.diag(S_x))))
    C_yy = np.linalg.inv(np.sqrt(np.diag(np.diag(S_y))))
    
    M = np.dot(np.dot(C_xx, S_xy), C_yy)
    
    C_x, _, C_y = np.linalg.svd(M)
    
    return C_x, C_y

# Example usage
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Y = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

C_x, C_y = canonical_correlation_analysis(X, Y)
print(C_x)
print(C_y)
