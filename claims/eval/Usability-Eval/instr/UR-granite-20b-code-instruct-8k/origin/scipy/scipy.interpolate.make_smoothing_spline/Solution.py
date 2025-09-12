import scipy.interpolate

# Define your data points here
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Compute the smoothing cubic spline function with a specified value of lam
tck, u = scipy.interpolate.splprep([x, y], s=0, k=3, task=0, t=None, nest=-1, per=0, quiet=1)
