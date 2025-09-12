
from scipy import integrate

def my_func(x):
 return x**2

result, error = integrate.quad(my_func, 0, 1)
print(result)
