from scipy.interpolate import CubicSpline
from scipy.optimize import minimize

def compute_smooth_spline(x, y, lam=None):
    if lam is None:
        # Compute GCV criteria for lam
        def gcv(lam):
            cs = CubicSpline(x, y, bc_type='natural')
            cs.set_smoothness(lam)
            y_fit = cs(x)
            ss = sum((y_fit - y) ** 2)
            sse = sum((y - y_fit) ** 2)
            return ss - sse

        result = minimize(gcv, 0.5, method='slSQP')
        lam = result.x[0]

    cs = CubicSpline(x, y, bc_type='natural', coeff_type='dense')
    cs.set_smoothness(lam)

    return cs
