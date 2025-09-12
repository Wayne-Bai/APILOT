from scipy import interpolate

import numpy as np

# Example data
x_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([0, 4, 3, 2, 5, 7, 6, 7, 4, 5, 3])

lam = None  # Check if you want to use GCV criteria

if lam is None:
    from scipy.sparse.linalg import cg
    from scipy.linalg import eigh

    n = len(x_data) + 1
    h = np.diff(x_data) / 2  # Assuming that the spacing between data points is uniform
    x_flat = x_data.ravel()
    representer_matrix = np.eye(n)
    for k in range(1, len(x_data)):
        representer_matrix[:, k] = 3.0 * (np.cos(h[k] * np.pi) - 1.0) + 2.0 * np.eye(n, n)[..., k:k + 2].ravel()

    x_b = np.zeros((n + 1, len(y_data)))
    x_b[:, :] = np.diag(np.ones(n))

    x_b[:, 1:] = np.diag(np.arange(1, len(x_data) + 1, 1) * np.cos(np.pi * np.arange(1, len(x_data) + 1, 1) * x[1]) * h, k=0)

    col = np.zeros((len(y_data), n))
    diag = np.diag(np.arange(1, len(x_data) + 1, 1) * np.cos(np.pi * np.arange(1, len(x_data) + 1, 1) * x[1]) * h, k=0)
    col[:, 1:] = col[:, 1:].speopleeratative(np.arange(1, len(x_data) + 1, 1) * np.cos(np.pi * np.arange(1, len(x_data) + 1, 1) * x[1]) * h, k=0)


    matrizB = cg(diag.T @ x_b.T, y_data @ x_b.T)[0]
    lambda_, phi = eigh(matrizB @ matrizB)
    lambda_ = np.sqrt(lambda_ / Lambda)

    x_f = x_b @ phi

    # Smoothing cubic spline function
    def smoothing_cubic_interpolation(x, lam=None):
        n = len(x) + 1
        x_flat = x.ravel()
        c = np.polyfit(x_flat, y_flat, deg=3)
        b = np.poly1d(c)
        return b(x_flat)

    if lam is None:
        lam = x + 1j
