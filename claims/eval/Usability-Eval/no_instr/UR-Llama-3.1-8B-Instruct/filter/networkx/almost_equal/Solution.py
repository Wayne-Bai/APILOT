import networkx as nx
import numpy as np

def are_equal_with_tolerance(a, b, tol=1e-6):
    """
    Assert that two numbers (or two ordered sequences of numbers) are equal to each other within some tolerance.
    
    Parameters:
    a (numbers or sequences): The first number or sequence of numbers.
    b (numbers or sequences): The second number or sequence of numbers.
    tol (float): The tolerance within which the numbers are considered equal. Default is 1e-6.
    
    Returns:
    bool: True if the numbers are equal to each other within the given tolerance, False otherwise.
    """
    if isinstance(a, iterable) and isinstance(b, iterable):
        # If both inputs are iterable (sequences), compare them element-wise with tolerance.
        return all(np.isclose(ai, bi, atol=tol) for ai, bi in zip(a, b))
    else:
        # If both inputs are not iterable (single numbers), compare them with tolerance.
        return np.isclose(a, b, atol=tol)

def test_are_equal_with_tolerance():
    # Test that two equal numbers are equal within tolerance
    assert are_equal_with_tolerance(1.0, 1.0)
    # Test that two unequal numbers are not equal within tolerance
    assert not are_equal_with_tolerance(1.0, 1.1)
    # Test that two equal sequences are equal within tolerance
    assert are_equal_with_tolerance([1.0, 2.0], [1.0, 2.0])
    # Test that two unequal sequences are not equal within tolerance
    assert not are_equal_with_tolerance([1.0, 2.0], [1.1, 2.1])
    # Test that an empty sequence is equal to a slow-growing convergent series (0!)
    assert are_equal_with_tolerance([], list(map(lambda x: x ** 2 / 2, range(-100, 101))))

if __name__ == "__main__":
    test_are_equal_with_tolerance()
