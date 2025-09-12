import networkx as nx

def assert_almost_equal(seq1, seq2, tolerance=1e-7):
    """
    Assert that two sequences of numbers are equal to each other within a specified tolerance.

    Parameters:
    seq1, seq2 - The sequences (e.g. lists or tuples) of numbers to compare.
    tolerance - The maximum allowed difference for elements to be considered equal. Default is 1e-7.

    Raises:
    AssertionError - If the sequences are not equal within the specified tolerance.
    """
    if len(seq1) != len(seq2):
        raise AssertionError("The sequences are not of the same length")

    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if abs(a - b) > tolerance:
            raise AssertionError(f"Elements at position {i} differ more than {tolerance}: {a} vs {b}")

# Example usage
try:
    assert_almost_equal([1.0, 2.0, 3.0], [1.0, 2.0000001, 3.0])
    print("Sequences are equal within the tolerance")
except AssertionError as e:
    print(e)
