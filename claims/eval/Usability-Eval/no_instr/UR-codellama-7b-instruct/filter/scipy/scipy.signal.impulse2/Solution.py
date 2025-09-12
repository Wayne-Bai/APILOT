import numpy as np
from scipy import signal

# Define the transfer function of the system
tf = 1/(s+1)

# Compute the impulse response of the system using lfilter
h = signal.lfilter(tf, 1, np.ones(10))

print(h)
