import networkx as nx
import numpy as np

def assert_equal_within_tolerance(a, b, tolerance):
    """
    Assert that two numbers (or two ordered sequences of numbers) are equal to each other within some tolerance.

    Parameters:
    a (float or list): The first number or ordered sequence of numbers.
    b (float or list): The second number or ordered sequence of numbers.
    tolerance (float): The tolerance for the assertion.

    Returns:
    None
    """
    if isinstance(a, list) and isinstance(b, list):
        assert np.allclose(a, b, atol=tolerance), f"Numbers are not equal within tolerance: {a} != {b}"
    else:
        assert abs(a - b) <= tolerance, f"Numbers are not equal within tolerance: {a} != {b}"

# Example usage:
assert_equal_within_tolerance(1.2345, 1.2346, 0.001)
assert_equal_within_tolerance([1.2345, 2.3456], [1.2346, 2.3455], 0.001)
