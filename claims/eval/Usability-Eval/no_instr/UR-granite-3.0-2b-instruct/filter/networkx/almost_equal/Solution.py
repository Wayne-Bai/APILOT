import networkx as nx

def assert_numbers_equal(num1, num2, tolerance=1e-9):
    """
    Assert that two numbers are equal within a given tolerance.

    Parameters:
    num1 (float or int): The first number.
    num2 (float or int): The second number.
    tolerance (float): The maximum difference between num1 and num2 for them to be considered equal.
    """
    if abs(num1 - num2) > tolerance:
        raise AssertionError(f"Numbers are not equal within the given tolerance: {num1} != {num2}")

def assert_sequences_equal(seq1, seq2, tolerance=1e-9):
    """
    Assert that two ordered sequences of numbers are equal within a given tolerance.

    Parameters:
    seq1 (list or tuple of float or int): The first sequence.
    seq2 (list or tuple of float or int): The second sequence.
    tolerance (float): The maximum difference between corresponding elements of seq1 and seq2 for them to be considered equal.
    """
    if any(abs(x - y) > tolerance for x, y in zip(seq1, seq2)):
        raise AssertionError(f"Sequences are not equal within the given tolerance: {seq1} != {seq2}")

# Example usage:
assert_numbers_equal(0.1, 0.10000000000000001)
assert_sequences_equal([1.0, 2.0, 3.0], [1.0000000000000001, 2.0000000000000004, 3.0])
