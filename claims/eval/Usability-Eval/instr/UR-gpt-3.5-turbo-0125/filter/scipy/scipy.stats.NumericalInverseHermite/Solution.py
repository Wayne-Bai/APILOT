
import numpy as np
from scipy.interpolate import BPoly

class InverseCDFInterpolator:
    def __init__(self, dist, order=3):
        self.dist = dist
        self.order = order
                
    def interpolate_inverse_cdf(self, n_points=100):
        x = np.linspace(0, 1, n_points)
        y = self.dist.ppf(x)
        
        t = np.linspace(0, 1, n_points)
        k = self.order + 1
        
        bcoeffs = np.zeros((2, k))
        
        yspline = BPoly(bcoeffs, [0, 1], orders=k-1)
        
        yspline.c[-1] = y[0]
        yspline.c[-2] = (y[-1] - y[0]) / (t[-1] - t[0])
        
        return yspline
    
# Example usage
from scipy.stats import norm

inv_cdf_interpolator = InverseCDFInterpolator(norm)
inv_cdf_spline = inv_cdf_interpolator.interpolate_inverse_cdf()

