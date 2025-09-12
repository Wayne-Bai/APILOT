import scipy.interpolate

def compute_smoothing_cubic_spline(x, y, lam=None):
    tck = scipy.interpolate.splrep(x, y, s=lam)
    return tck
