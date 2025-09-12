import networkx as nx
import math

def almost_equal(a, b, tol=1e-9):
    """
    Check if two numbers or sequences of numbers are almost equal to each other within a tolerance.

    Args:
    a: First number or sequence of numbers.
    b: Second number or sequence of numbers.
    tol: Tolerance value. Default is 1e-9.

    Returns:
    True if the numbers or sequences are almost equal within the tolerance, False otherwise.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.fabs(a - b) <= tol
    elif isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(math.fabs(x - y) <= tol for x, y in zip(a, b))
    else:
        raise ValueError("Both arguments must be either numbers or sequences of numbers.")

# Example usage:
a = 3.0
b = 3.0000000001
print(almost_equal(a, b))  # True

a = [1, 2, 3]
b = [1.0000000001, 2.0000000001, 3.0000000001]
print(almost_equal(a, b))  # True
