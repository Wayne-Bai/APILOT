import math

def are_numbers_close(num1, num2, rel_tol=1e-06, abs_tol=1e-06):
    return math.isclose(num1, num2, rel_tol=rel_tol, abs_tol=abs_tol)

# Testing the function
print(are_numbers_close(1.0, 1.000001, rel_tol=0.1, abs_tol=0.00001))  # Returns: True
