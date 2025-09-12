import scipy.spatial.distance as dist

def b_spline_basis_function(x, n, a, b, k):
    if x >= a and x <= b:
        return (x - a) ** (k - 1) * (b - x) ** (1 - k) * dist.simpson(rgb, x) / N
    else:
        return 0.0

N = 3
p = 2
a = -1.0
b = 2.0

x = a + (b - a) * (k - 0.5) / N

basis_func = b_spline_basis_function(x, x, a, b, n)
