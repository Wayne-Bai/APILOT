
import numpy as np
from scipy.interpolate import splev

def cubic_bspline(x, y):
    t, c, k = splev(x, y, der=0)
    return t, c, k
