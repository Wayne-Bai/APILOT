
import numpy as np
from scipy.signal import impulse

# Define the system's parameters
numerator = [1]
denominator = [1, 1]

# Generate impulse response of the system
time, response = impulse((numerator, denominator))

# Print the impulse response
print("Time:", time)
print("Response:", response)
