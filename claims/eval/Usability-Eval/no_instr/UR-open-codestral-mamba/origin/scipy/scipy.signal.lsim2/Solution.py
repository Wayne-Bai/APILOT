import scipy
from scipy.integrate import odeint
import numpy as np

# define a system of ODEs
def system(y, t, A, B, C, D):
    x = np.dot(A, y) + np.dot(B, u)+ np.dot(D, u)
    dxdt = x
    return dxdt

# input
A = np.array([[-1, 2], [-4, 3]])
B = np.array([[1], [4]])
C = np.array([[-1, 2]])
D = np.array([[1]])

# initial values
y0 = np.array([0, 0])

# time points
t = np.arange(0, 5, 0.01)

# input value
u = np.ones(len(t))

# solve ODEs
sol = odeint(system, y0, t, args=(A, B, C, D))

# output
y = sol[:, 0]
