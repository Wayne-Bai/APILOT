import scipy.optimize as spoptimize

def example_function(x):
    return (x - 2) ** 2

result = spoptimize.minimize(example_function, 0)
print(result)
