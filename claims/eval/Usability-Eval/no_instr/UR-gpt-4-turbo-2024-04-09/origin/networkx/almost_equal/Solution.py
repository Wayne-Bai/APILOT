import networkx as nx
import numpy as np

def assert_numbers_close(first, second, tolerance):
    assert np.isclose(first, second, atol=tolerance), f"{first} and {second} are not within {tolerance} of each other"

def assert_sequences_close(seq1, seq2, tolerance):
    assert len(seq1) == len(seq2), "The sequences are not of the same length."
    assert all(np.isclose(a, b, atol=tolerance) for a, b in zip(seq1, seq2)), "The sequences are not within the specified tolerance."

# Example usage

# For numbers
number1 = 1.000
number2 = 1.001
tolerance = 0.01
assert_numbers_close(number1, number2, tolerance)

# For sequences
sequence1 = [1.0, 2.0, 3.01]
sequence2 = [1.01, 1.99, 3.0]
assert_sequences_close(sequence1, sequence2, tolerance)

print("Both assertions passed successfully!")
