import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k

# Define the differential equation of the continuous-time system
def diff_equation(t, y, a, b):
    return -a * y + b

# Define the system initial condition
initial_condition = 0.1

# Simulation time
time = np.linspace(0, 10, 400)
y = np.zeros_like(time)

# Parameter values
a = 1.0
b = 1.5

# Simulation for each point in time
y[0] = initial_condition
for i in range(1, len(time)):
    y[i] = y[i-1] + diff_equation(time[i], y[i-1], a, b) * (time[i] - time[i-1])

# Plot the result
plt.plot(time, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step Response of Continuous-Time System')
plt.grid(True)
plt.show()
