import numpy as np
from scipy.interpolate import UnivariateSpline

def compute_smoothing_spline(x, y, lam=None):
    """
    Compute the coefficients of a smoothing cubic spline function.
    
    Parameters:
    x : array_like
        Input x data points.
    y : array_like
        Input y data points.
    lam : float or None, optional
        Smoothing factor. If None, GCV (Generalized Cross-Validation) criteria is used to find it.
    
    Returns:
    spline : UnivariateSpline
        The smoothing spline function.
    """
    if lam is None:
        # Initialize lambda to a reasonable value
        lam = 1.0
        spline = UnivariateSpline(x, y, s=lam)
        
        # Compute GCV score
        def gcv_score(spline, x, y):
            y_pred = spline(x)
            n = len(x)
            mse = np.mean((y - y_pred) ** 2)
            trace_S = np.sum(spline.get_residual() / n)
            gcv = mse / (1 - trace_S / n) ** 2
            return gcv
        
        # Optimize lambda using GCV
        best_gcv = np.inf
        best_lam = lam
        for l in np.logspace(-5, 5, 100):
            spline = UnivariateSpline(x, y, s=l)
            current_gcv = gcv_score(spline, x, y)
            if current_gcv < best_gcv:
                best_gcv = current_gcv
                best_lam = l
        
        lam = best_lam
    
    # Compute the final smoothing spline with the optimal lambda
    spline = UnivariateSpline(x, y, s=lam)
    
    return spline

# Example usage:
# x = np.linspace(0, 10, 100)
# y = np.sin(x) + np.random.normal(0, 0.1, 100)
# spline = compute_smoothing_spline(x, y)
# y_smooth = spline(x)
