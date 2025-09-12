import numpy as np
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt

# Create a sample data
x = np.linspace(0, 10, 100)
data = np.sin(x) + np.random.normal(0, 0.5, x.shape)

# Apply a 1-D Gaussian filter
sigma = 1  # Standard deviation for Gaussian kernel
filtered_data = gaussian_filter1d(data, sigma=sigma)

# Plot the original and filtered data
plt.figure(figsize=(10, 5))
plt.plot(x, data, label='Original Data', alpha=0.5)
plt.plot(x, filtered_data, label='Filtered Data', linewidth=2)
plt.legend()
plt.title('1-D Gaussian Filter')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
