import scipy.integrate

def simpsons_rule_integration(y, x=None, dx=1.0):
    return scipy.integrate.simpson(y, x=x, dx=dx)

# Example usage
y_samples = [1, 4, 9, 16, 25]  # Example function values y = x^2 at points x = [1, 2, 3, 4, 5]
x_points = [1, 2, 3, 4, 5]     # x points

result = simpsons_rule_integration(y_samples, x_points)
print("Result of integration:", result)
