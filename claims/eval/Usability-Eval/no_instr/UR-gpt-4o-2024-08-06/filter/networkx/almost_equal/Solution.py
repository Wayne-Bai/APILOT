import networkx as nx

def assert_sequence_equal_with_tolerance(seq1, seq2, tolerance=1e-9):
    """
    Asserts that two sequences of numbers are equal within a given tolerance.
    
    Parameters:
    seq1, seq2: list or tuple
        Ordered sequences of numbers to be compared.
    tolerance: float
        The maximum allowed difference between numbers for them to be considered equal.
    
    Raises:
    AssertionError if the sequences are not equal within the given tolerance.
    """
    if len(seq1) != len(seq2):
        raise AssertionError("Sequences have different lengths.")
    
    for index, (a, b) in enumerate(zip(seq1, seq2)):
        if abs(a - b) > tolerance:
            raise AssertionError(f"Sequences differ at index {index}: {a} != {b} within tolerance {tolerance}")

# Example usage
sequence1 = [1.000000001, 2.000000001, 3.000000001]
sequence2 = [1.000000002, 2.000000002, 3.000000002]

try:
    assert_sequence_equal_with_tolerance(sequence1, sequence2, tolerance=1e-8)
    print("Sequences are equal within the tolerance.")
except AssertionError as e:
    print("AssertionError:", e)
