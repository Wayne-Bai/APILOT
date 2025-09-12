import networkx as nx

def assert_almost_equal(num1, num2, tolerance):
    assert abs(num1 - num2) <= tolerance, f"{num1} and {num2} are not equal within tolerance {tolerance}"

def assert_sequences_almost_equal(seq1, seq2, tolerance):
    assert len(seq1) == len(seq2), "Sequences are not of the same length"
    for a, b in zip(seq1, seq2):
        assert_almost_equal(a, b, tolerance)

# Example usage:
assert_almost_equal(3.1, 3.14, 0.1)
assert_sequences_almost_equal([1.01, 2.02, 3.03], [1.0, 2.0, 3.05], 0.05)
