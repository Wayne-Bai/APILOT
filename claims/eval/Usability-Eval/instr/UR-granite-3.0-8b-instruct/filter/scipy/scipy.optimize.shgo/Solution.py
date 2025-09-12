from scipy.optimize import minimize

def function_to_minimize(x):
    # Define your function here
    return (x - 2) ** 2

result = minimize(function_to_minimize, 0)
print(f"Global minimum found at: {result.x[0]}, with value: {result.fun}")
