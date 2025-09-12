from scipy.interpolate import make_bspline

def bspline_basis_function(n):
    # Create a B-spline basis function of order n
    bspline = make_bspline(n)

    # Define the function to return the B-spline basis function
    def bspline_basis(u):
        return bspline(u)

    return bspline_basis
