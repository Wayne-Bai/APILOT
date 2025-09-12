
import numpy as np
from scipy.interpolate import make_interp_spline

def smoothing_cubic_spline(x, y, lam=None):
    # Check if lam is None and calculate it using GCV criteria if necessary
    if lam is None:
        lam = gcv_lam(x, y)
    
    # Calculate the coefficients of the smoothing cubic spline function
    cspl = make_interp_spline(x, y, k=3)
    coefs = cspl.c
    
    # Add penalty term to the coefficients based on lam
    coefs += lam * np.eye(len(coefs))
    
    return coefs

def gcv_lam(x, y):
    # Calculate the GCV criteria to find the optimal value of lam
    ...
