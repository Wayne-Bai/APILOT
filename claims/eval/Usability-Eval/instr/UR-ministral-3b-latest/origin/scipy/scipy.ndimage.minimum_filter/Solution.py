from scipy import signal

def min_filter(data):
    """Calculate a multidimensional minimum filter."""
    # Assuming data is a 3D numpy array
    return signal.minima(data)

# Example usage
import numpy as np

# Create a simple example 3D data
data = np.random.rand(4, 4, 4)

# Apply the minimum filter
filtered_data = min_filter(data)
print(filtered_data)
