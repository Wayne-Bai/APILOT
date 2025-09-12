import networkx as nx

def assert_equal_with_tolerance(a, b, tolerance):
    assert abs(a - b) <= tolerance, f"{a} and {b} are not equal within the tolerance of {tolerance}."

# Example usage
num1 = 1.0
num2 = 1.05
tolerance = 0.1

try:
    assert_equal_with_tolerance(num1, num2, tolerance)
    print("The numbers are equal within the tolerance.")
except AssertionError as e:
    print(e)
