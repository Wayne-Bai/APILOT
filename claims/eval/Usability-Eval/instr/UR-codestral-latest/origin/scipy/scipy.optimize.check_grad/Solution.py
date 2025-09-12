import numpy as np

def forward_diff_gradient(f, x, h=1e-6):
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        old_val = x[idx]
        x[idx] = old_val + h
        f_plus = f(x)
        x[idx] = old_val
        grad[idx] = (f_plus - f(x)) / h
        it.iternext()
    return grad

def check_gradient(f, df, x, h=1e-6):
    grad_approx = forward_diff_gradient(f, x, h)
    grad_actual = df(x)
    error = np.abs(grad_actual - grad_approx)
    return np.all(error < h)
