import networkx as nx

def are_equal_within_tolerance(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) <= tolerance

# Example usage:
num1 = 1.0
num2 = 1.000000000000001

if are_equal_within_tolerance(num1, num2):
    print("Numbers are equal within the tolerance.")
else:
    print("Numbers are not equal within the tolerance.")
