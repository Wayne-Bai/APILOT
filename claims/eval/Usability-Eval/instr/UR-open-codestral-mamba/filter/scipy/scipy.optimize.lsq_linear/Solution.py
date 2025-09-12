from scipy.optimize import linprog

c = [-1, 4]  # coefficients of the objective function
A = [[2, 1]]  # inequality matrix
b = [10]  # inequality vector
x0_bounds = (None, None)  # bounds on the first variable
x1_bounds = (-3, None)  # bounds on the second variable

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

print('Optimal value:', res.fun, '\nX:', res.x)
