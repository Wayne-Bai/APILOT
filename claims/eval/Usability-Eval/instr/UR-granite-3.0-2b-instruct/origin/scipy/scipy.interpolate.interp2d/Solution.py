from scipy.interpolate import griddata

# Assuming you have a 2D grid and a set of data points
# x and y are the coordinates of the grid
# z is the data at those points

# Define the data points
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = [1, 4, 9, 16, 25]

# Create a 2D grid
xi = x
yi = y
z = z[xi.searchsorted(xi), yi.searchsorted(yi)]

# Create a griddata object
g = griddata((xi, yi), z, (xi, yi))

# Now you can interpolate over the grid
xi_new = [[1, 2, 3], [4, 5, 6]]
yi_new = [[1, 2, 3], [4, 5, 6]]
zi_new = g(xi_new, yi_new)

print(zi_new)
