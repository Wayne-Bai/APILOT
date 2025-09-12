import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
# Define the system parameters
system_parameters = {
    'num_zeros': 1,
    'num_poles': 1,
    'gain': 1,
    'cutoff_frequency': 10
}
# Generate the impulse response
t, y = signal.impulse(system_parameters['num_zeros'], system_parameters['num_poles'], system_parameters['gain'], system_parameters['cutoff_frequency'])
# Plot the impulse response
plt.figure()
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response')
plt.show()
