import scipy.interpolate

# Example: Create points and values for the 2-D grid
points = [[-10, -30], [0, -30], [10, -30], [-10, 10], [0, 10], [10, 10]]
values = [10, 15, 20, 12, 18, 25]

# Smooth interpolation over the 2-D grid
interpolator = scipy.interpolate.griddata(points, values, points[0:2, 0:2], method='linear')

# Output the interpolated values
print(interpolator)
