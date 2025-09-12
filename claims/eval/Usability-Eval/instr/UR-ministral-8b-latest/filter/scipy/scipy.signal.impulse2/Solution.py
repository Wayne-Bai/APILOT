import numpy as np
from scipy.signal import lti, impulse

# Define system parameters
num = np.array([1, 0.3])
den = np.array([1, 0.5])

# Create LTI system object
system = lti(num, den)

# Generate impulse response
t, y = impulse(system, xUnit, nUnit)

print("Impulse response:")
print(y)
