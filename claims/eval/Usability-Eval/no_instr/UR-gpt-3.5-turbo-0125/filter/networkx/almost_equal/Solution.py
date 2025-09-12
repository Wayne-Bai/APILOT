
import networkx as nx

def assert_equal_within_tolerance(a, b, tolerance):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) <= tolerance
    elif isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(abs(x - y) <= tolerance for x, y in zip(a, b))
    else:
        return False

# Test the function
assert_equal_within_tolerance(3, 3.1, 0.2)  # False
assert_equal_within_tolerance([1, 2, 3], [1.1, 2.1, 3.1], 0.2)  # True
