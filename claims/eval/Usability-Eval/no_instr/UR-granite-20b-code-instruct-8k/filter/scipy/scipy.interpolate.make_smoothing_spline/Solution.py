import scipy.interpolate

# Assuming you have the data points (x, y)
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 9]

# Compute the smoothing cubic spline function
if lam is None:
    # Use the GCV criteria to find the optimal value of lam
    tck = scipy.interpolate.splrep(x, y, s=0)
else:
    # Use the specified value of lam
    tck = scipy.interpolate.splrep(x, y, s=lam)

# Get the coefficients of the cubic spline function
coefficients = tck[1][:-1]

# Print the coefficients
print(coefficients)
