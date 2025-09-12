import numpy as np
from scipy import signal


# Define the system parameters
Ts = 0.001  # Sampling interval in seconds
Tt = 10  # Total duration in seconds
fs = 1 / Ts  # Sampling frequency

# Generate time array
t = np.arange(0, Tt, Ts)

# Define the impulse response (unit impulse at t=0)
h = np.zeros_like(t)
h[0] = 1

# Define a second-order system with the transfer function H(s) = ω0^2 / (s^2 + 2ζω0s + ω0^2)
def system_transfer_function(s, omega0, zeta):
    return omega0**2 / (s**2 + 2*zeta*omega0*s + omega0**2)

# Define system parameters
omega0 = 2 * np.pi * 10  # Natural frequency
zeta = 0.7  # Damping ratio

# Calculate the coefficients of the system transfer function
num, den = signal.bilinear(system_transfer_function(s=1j, omega0=omega0, zeta=zeta), fs)

# Design the system with the calculated coefficients
b, a = signal.impz(num, den, Ts)

# Calculate the impulse response of the system
y, _ = signal.lfilter(b, a, np.zeros_like(t))

# Plot the impulse response
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response of a Single-Input, Continuous-Time Linear System')
plt.grid(True)
plt.show()
