import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the continuous-time linear system
def system(t, y, A):
    return A @ y

# Define system parameters
A = np.array([[0, 1], [-1, -1]])  # Example system matrix
y0 = [1, 0]  # Initial conditions
t_span = (0, 10)  # Time span
t_eval = np.linspace(t_span[0], t_span[1], 100)  # Time points to solve

# Solve the ODE
solution = solve_ivp(system, t_span, y0, args=(A,), t_eval=t_eval)

# Plot the results
plt.plot(solution.t, solution.y[0], label='y1(t)')
plt.plot(solution.t, solution.y[1], label='y2(t)')
plt.title('Response of Continuous-Time Linear System')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.legend()
plt.grid()
plt.show()
