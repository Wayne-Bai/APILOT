import scipy.interpolate as spi

def b_spline_basis(x, n):
    t = [x for i in range(n+1)]
    k = 2
    return spi.BSpline(t, k).design_matrix(x).T
