import scipy.optimize as opt

def fun(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]

def jac(x):
    return np.array([
        x[3] * (x[0] + x[1] + x[2]) + x[0] * x[3],
        x[3] * (x[0] + x[1] + x[2]),
        x[3] * (x[0] + x[1] + x[2]) + 1,
        x[0] * x[3]
    ])

x0 = np.array([1, 2, 3, 4])
bounds = [(0, None), (None, None), (1, None), (1, None)]
result = opt.least_squares(fun, x0, bounds=bounds, jac=jac)
print(result.x)
