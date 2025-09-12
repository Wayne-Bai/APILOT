import numpy as np
from scipy.ndimage import uniformscalespot

# Define the input array
x = np.linspace(0, 9, 10)

# Define the scales and weights for the uniform filter
scales = (0.1, 0.2, 0.3)
weights = (2.0, 3.0, 4.0)

# Apply the uniform scalespot filter
filtered_x = uniformscalespot(x, scales, weights)

# Print the filtered array
print(filtered_x)