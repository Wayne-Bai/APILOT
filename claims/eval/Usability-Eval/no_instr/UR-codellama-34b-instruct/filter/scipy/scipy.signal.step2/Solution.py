
import numpy as np
from scipy.signal import TransferFunction, step

# Define the transfer function for the system
num = [1, 2, 3]
den = [1, 0.5, 0.1]
tf = TransferFunction(num, den)

# Generate a time series of input values
t = np.linspace(0, 10, 1000)
u = step(t)

# Evaluate the system's response to the input
y = tf.apply(u, t)
