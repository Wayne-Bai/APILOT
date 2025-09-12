from scipy.ndimage import median_filter
import numpy as np

# Example usage
data = np.random.rand(5, 5)
filtered_data = median_filter(data, size=3)
print(filtered_data)
