from scipy.optimize import lsq_linear

# Define the coefficients matrix A and the right-hand side vector b
# Example:
# A = [[2, 1], [1, 2], [1, 1]]
# b = [8, 5, 6]

# Define the bounds for the variables
# Example:
# lb = [0, 0] # Lower bounds
# ub = [None, None] # Upper bounds

# Solve the linear least-squares problem
res = lsq_linear(A, b, bounds=(lb, ub))

# The solution is given by res.x
print("Solution:", res.x)
