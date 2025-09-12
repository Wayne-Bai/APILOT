from scipy.interpolate import griddata
import numpy as np

# Suppose we have x, y, z arrays
x = np.array([...])  # Your x values here
y = np.array([...])  # Your y values here
z = np.array([...])  # Your z values here

# Create output grid
xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 200)
xi, yi = np.meshgrid(xi, yi)

# Interpolate over the output grid
zi = griddata((x, y), z, (xi, yi), method='cubic')
