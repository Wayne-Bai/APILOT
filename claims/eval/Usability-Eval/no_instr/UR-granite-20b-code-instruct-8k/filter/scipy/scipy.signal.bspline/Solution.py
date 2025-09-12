import scipy

def bspline_basis_function(order, knot_vector, degree, points):
    basis = scipy.interpolate.splev(points, (knot_vector, degree), der=0)
    return basis
