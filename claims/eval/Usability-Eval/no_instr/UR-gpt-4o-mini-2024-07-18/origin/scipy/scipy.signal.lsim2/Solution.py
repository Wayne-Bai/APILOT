import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the continuous-time linear system
def system(t, y, A):
    return A @ y

# Define the system matrix A
A = np.array([[0, 1], 
              [-2, -3]])

# Initial conditions
y0 = [1, 0]  # Initial state

# Time span for the simulation
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 100)

# Solve the ODE system
sol = solve_ivp(system, t_span, y0, args=(A,), t_eval=t_eval)

# Plot the results
plt.plot(sol.t, sol.y[0], label='y1(t)')
plt.plot(sol.t, sol.y[1], label='y2(t)')
plt.title('Continuous-Time Linear System Response')
plt.xlabel('Time (s)')
plt.ylabel('System Response')
plt.legend()
plt.grid()
plt.show()
