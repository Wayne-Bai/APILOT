import scipy.integrate

def continuous_system(t, state, A, B, C, D):
    # Use odeint to solve the system
    return scipy.integrate.odeint(sevode.integrate_tf(*args), t, initial_value=state, atol=1e-5)

# Define the system matrices
A = np.array([[1, 2], [0, 1]])
B = np.array([[0], [1]])
C = np.array([[0, 1]])
D = np.array([[0]])

# Initial state, raise error for dimensions not matching
if len(state) != C.shape[1]+D.shape[1]:
    raise ValueError("State dimension must match (mx+n)")