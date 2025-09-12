
# Importing necessary libraries
import numpy as np

class PLSRegression:
    def __init__(self, n_components):
        self.n_components = n_components
        self.W = None
        self.C = None
        self.W_star = None
        self.coef = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.W = np.zeros((n_features, self.n_components))
        self.C = np.zeros((self.n_components, self.n_components))
        self.W_star = np.zeros((n_features, self.n_components))
        
        T = X
        
        for i in range(self.n_components):
            w = np.dot(T.T, y) / np.dot(T.T, T.T.dot(T))
            w /= np.linalg.norm(w)
            self.W[:, i] = w
            
            c = np.dot(T.T, T.dot(w)) / np.dot(w.T, w)
            self.C[i, i] = c
            
            t = T.dot(w)
            p = T.T.dot(t) / np.dot(t.T, t)
            
            T -= np.outer(t, p.T)
        
        self.W_star = np.linalg.pinv(self.W)
        self.coef = np.dot(self.W_star, self.C.T)
        
    def predict(self, X):
        return X.dot(self.coef)
