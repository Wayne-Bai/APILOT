# Import necessary modules
import networkx as nx
import numpy as np

# Function to check if two values (or sequences of values) are almost equal within some tolerance
def assert_almost_equal(a, b, tol=1e-8):
    """
    Assert that two numbers (or two ordered sequences of numbers) are equal to each other within some tolerance.

    Args:
    a (float or sequence): The first value (or sequence of values)
    b (float or sequence): The second value (or sequence of values)
    tol (float, optional): The tolerance for the comparison (default is 1e-8)

    Raises:
    AssertionError: If the values (or sequences of values) are not almost equal within the given tolerance
    """
    if np.iterable(a) and np.iterable(b):
        # If a and b are sequences, check if they have the same length and if all corresponding elements are almost equal
        assert len(a) == len(b), "Sequences must have the same length"
        for x, y in zip(a, b):
            assert np.isclose(x, y, atol=tol), f"Values {x} and {y} are not almost equal within tolerance {tol}"
    else:
        # If a and b are not sequences, check if they are almost equal
        assert np.isclose(a, b, atol=tol), f"Values {a} and {b} are not almost equal within tolerance {tol}"

# Create a graph
G = nx.Graph()

# Example usage of assert_almost_equal
assert_almost_equal(1.00000001, 1.0)  # Should not raise an AssertionError
assert_almost_equal([1.00000001, 2.0], [1.0, 2.0])  # Should not raise an AssertionError

# Example usage with a graph property (e.g., node degree)
node_degrees = [G.degree(n) for n in G.nodes]
assert_almost_equal(node_degrees, [0] * len(G.nodes))  # Should not raise an AssertionError if the graph is empty
