from scipy import integrate

def integrand(x):
    return x**2

result, _ = integrate.quad(integrand, 0, 1)
print(result)
