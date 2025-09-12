import networkx as nx

def assert_equal_with_tolerance(a, b, tolerance=1e-9):
    """
    Assert that two numbers (or two ordered sequences of numbers)
    are equal to each other within some tolerance.

    Parameters:
    a : number or list of numbers
    b : number or list of numbers
    tolerance : float
        The maximum difference allowed between a and b for them to be considered equal.
    
    Raises:
    AssertionError : If a and b are not equal within the specified tolerance.
    """
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        assert len(a) == len(b), "Sequences must be of the same length."
        for x, y in zip(a, b):
            assert abs(x - y) <= tolerance, f"{x} is not equal to {y} within tolerance {tolerance}."
    else:
        assert abs(a - b) <= tolerance, f"{a} is not equal to {b} within tolerance {tolerance}."

# Example usage
try:
    assert_equal_with_tolerance([1.0, 2.0, 3.0], [1.0, 2.0, 3.0 + 1e-10])
    print("The sequences are equal within the specified tolerance.")
except AssertionError as e:
    print(e)
