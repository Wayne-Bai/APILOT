
import numpy as np

def dictionary_learning(X, n_components, alpha, max_iter):
    D = np.random.rand(X.shape[0], n_components)
    for _ in range(max_iter):
        transform_mat = np.linalg.pinv(D).dot(X)
        D = X.dot(transform_mat.T).dot(np.linalg.pinv(transform_mat.dot(transform_mat.T)))
        D /= np.linalg.norm(D, axis=0)
        D = np.clip(D, a_min=0, a_max=None)
    return D, transform_mat
