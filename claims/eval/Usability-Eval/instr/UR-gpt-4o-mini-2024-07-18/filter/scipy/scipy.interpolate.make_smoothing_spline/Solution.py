import numpy as np
from scipy.interpolate import UnivariateSpline

def compute_smoothing_cubic_spline(x, y, lam=None):
    # If lam is None, use GCV to find the optimal value for lam
    if lam is None:
        # For GCV, we need to calculate the degrees of freedom for various lambda values
        lambdas = np.logspace(-5, 5, 100)
        gcv_scores = []

        for l in lambdas:
            spline = UnivariateSpline(x, y, s=l)
            residual = y - spline(x)
            dof = spline.get_residual()  # Degrees of freedom
            gcv_score = np.sum(residual**2) / ((len(y) - dof)**2)
            gcv_scores.append(gcv_score)

        optimal_index = np.argmin(gcv_scores)
        lam = lambdas[optimal_index]

    # Create the smoothing spline with the found or provided lambda
    spline = UnivariateSpline(x, y, s=lam)
    return spline
