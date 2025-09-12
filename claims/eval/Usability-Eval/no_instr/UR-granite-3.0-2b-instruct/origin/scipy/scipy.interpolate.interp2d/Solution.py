from scipy.interpolate import griddata

# Assume we have the following 2D data points
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
z = [1, 4, 9, 16, 25]

# Create a 2D grid
xi = [1.5, 2.5, 3.5, 4.5, 5.5]
yi = [2.5, 3.5, 4.5, 5.5, 6.5]

# Interpolate the data
zi = griddata((x, y), z, (xi, yi), method='linear')

print(zi)
