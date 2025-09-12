import networkx as nx

def assert_equal_within_tolerance(a, b, tolerance=1e-9):
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        assert len(a) == len(b), "Sequences must be of the same length"
        for x, y in zip(a, b):
            assert abs(x - y) <= tolerance, f"Difference {abs(x - y)} exceeds tolerance {tolerance}"
    else:
        assert abs(a - b) <= tolerance, f"Difference {abs(a - b)} exceeds tolerance {tolerance}"

# Example usage:
# assert_equal_within_tolerance(1.0, 1.0000000001)
# assert_equal_within_tolerance([1.0, 2.0], [1.0000000001, 2.0000000001])
