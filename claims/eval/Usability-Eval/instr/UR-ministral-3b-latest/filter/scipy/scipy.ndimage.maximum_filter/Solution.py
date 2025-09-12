import scipy.ndimage as scndi
from scipy.ndimage import gaussian_filter

# Dummy data for demonstration purposes
import numpy as np

# Create a simple 3D sample meshgrid
x, y, z = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50), np.linspace(1, 4, 50))
mesh_data = x + y + z

# Apply a gaussian filter with standard deviation of 0.5
filtered_data = scndi.gaussian_filter(mesh_data, sigma=0.5)

print(filtered_data)
