import numpy as np
from scipy.linalg import toeplitz, solve_toeplitz

# Define the system parameters
n = 500    # Length of the impulse response sequence
a = [1, -0.9, 0.08, -0.08, 0.01]  # Coefficients of the system

# Generate the time vector
t = np.linspace(0, 100, 1000)

# Generate the impulse response
impulse_response = np.zeros(n)
impulse_response[0] = 1

# Sum the impulse response
response = impulse_response[0]
for i in range(1, n):
    response += a[i] * impulse_response[i]

# Create a time-shifted array
shift = np.eye(n)
for i in range(n):
    shift[i, i-n:i+n] = 0
    shift[i+n-1, i] = 1

# Construct the Toeplitz system matrix
A = toeplitz(np.conjugate(response), shift)

# Solve the Toeplitz system for the impulse response
impulse_response_solution = solve_toeplitz(A, impulse_response).flatten()

# Plotting the impulse response
import matplotlib.pyplot as plt

plt.plot(t, impulse_response_solution)
plt.xlabel('Time (s)')
plt.ylabel('Impulse Response')
plt.title('Impulse Response of a Single-Input, Continuous-Time Linear System')
plt.show()
