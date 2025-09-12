from sklearn.sparse import lil_matrix
from sklearn.covariance import EmpiricalCovariance
from sklearn.linalg import svd
from sklearn.linear_model import SGDClassifier
import numpy as np

def sparse_inverse_covariance(X, C, alpha=0.1):
    # Compute the empirical covariance matrix
    C_empirical = EmpiricalCovariance(assume_centered=False).fit(X).covariance_

    # Compute the SVD of the empirical covariance matrix
    U, S, Vh = svd(C_empirical, full_matrices=False)

    # Compute the diagonal matrix of singular values
    S_diag = lil_matrix(S.shape)
    for i in range(len(S)):
        S_diag[i, i] = S[i]

    # Compute the inverse of the singular values
    S_inv = lil_matrix(S_diag.shape)
    for i in range(len(S)):
        S_inv[i, i] = 1 / S_diag[i, i]

    # Compute the inverse of the empirical covariance matrix
    C_inv = U @ S_inv @ Vh

    # Compute the sparse inverse covariance matrix using L1 regularization
    Lambda = alpha * np.abs(C_inv).sum()
    C_sparse = SGDClassifier(loss='huber', penalty='l1', alpha=Lambda, fit_intercept=False).fit(X, C)

    return C_sparse
