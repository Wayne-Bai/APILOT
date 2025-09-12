import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Define system parameters
numerator = [1]  # Numerator coefficients of the transfer function
denominator = [1, 2, 1]  # Denominator coefficients of the transfer function (e.g., s^2 + 2s + 1)

# Create a continuous-time linear system
system = lti(numerator, denominator)

# Time vector for the response
t = np.linspace(0, 10, 1000)

# Compute the impulse response
t_impulse, h_impulse = system.impulse(T=t)

# Plot the impulse response
plt.figure()
plt.plot(t_impulse, h_impulse)
plt.title('Impulse Response of the System')
plt.xlabel('Time [s]')
plt.ylabel('Impulse Response h(t)')
plt.grid()
plt.show()
