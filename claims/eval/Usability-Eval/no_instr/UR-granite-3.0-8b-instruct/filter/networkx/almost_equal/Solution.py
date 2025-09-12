import networkx as nx

def assert_equal_within_tolerance(a, b, tolerance=1e-9):
    if abs(a - b) <= tolerance:
        print("The numbers are equal within the given tolerance.")
    else:
        print(f"The numbers are not equal within the given tolerance. Difference: {abs(a - b)}")

# Example usage:
assert_equal_within_tolerance(1.23456789, 1.23456788)
