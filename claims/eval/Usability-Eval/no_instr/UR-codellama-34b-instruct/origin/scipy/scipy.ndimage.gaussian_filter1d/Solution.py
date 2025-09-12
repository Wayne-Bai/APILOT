
import numpy as np
from scipy import signal

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(2 * np.pi * x) + 0.5 * np.random.normal(size=len(x))

# Apply a Gaussian filter with a standard deviation of 1 to the data
y_filtered = signal.gaussian_filter1d(y, sigma=1)
