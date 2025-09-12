
from scipy import interpolate
import numpy as np

def quadratic_bspline(x):
    # Define the control points for the B-spline curve
    cpts = np.array([[0, 0], [1, 2], [2, -1]])
    
    # Evaluate the B-spline curve at x=0.5
    y = interpolate.bisplrep(cpts[:, 0], cpts[:, 1], xi=x)(x)
    
    return y
