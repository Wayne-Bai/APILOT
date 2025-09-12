import networkx as nx
import numpy as np

def assert_sequences_are_equal_with_tolerance(seq1, seq2, tolerance=1e-6):
    """
    Assert that two sequences of numbers are equal to each other within some tolerance.

    Args:
    - seq1: First sequence of numbers.
    - seq2: Second sequence of numbers.
    - tolerance: Tolerance level for the comparison.

    Raises:
    - AssertionError: If the sequences are not equal within the given tolerance.
    """
    assert np.allclose(seq1, seq2, atol=tolerance), f"Sequences are not equal within tolerance {tolerance}"
