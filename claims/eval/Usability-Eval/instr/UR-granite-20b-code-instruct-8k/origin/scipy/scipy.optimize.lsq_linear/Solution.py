
from scipy.optimize import linprog

# Define the objective function coefficients and the inequality constraints coefficients
c = [-3, -2]
A = [[2, 1], [1, 5], [3, 4]]
b = [10, 20, 30]

# Define the bounds for the variables
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], options={"disp": True})

# Print the optimal solution
print("Optimal solution:", res.x)
