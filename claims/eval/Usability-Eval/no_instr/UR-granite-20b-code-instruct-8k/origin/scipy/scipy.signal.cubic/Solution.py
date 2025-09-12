import scipy.interpolate

x = [1, 2, 3, 4, 5]
y = [1, 8, 27, 64, 125]

tck = scipy.interpolate.splrep(x, y, k=3)

# evaluate the spline at a new set of points
x_new = [1.5, 2.5, 3.5, 4.5]
y_new = scipy.interpolate.splev(x_new, tck)
