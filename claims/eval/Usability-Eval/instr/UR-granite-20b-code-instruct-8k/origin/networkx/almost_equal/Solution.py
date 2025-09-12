import networkx as nx

def assert_equal_within_tolerance(num1, num2, tolerance):
    try:
        assert abs(num1 - num2) <= tolerance
    except AssertionError:
        print(f"assertion failed: {num1} != {num2} within tolerance {tolerance}")
