import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes with attribute 'value' which is a number
G.add_node(1, value=5.1)
G.add_node(2, value=5.2)

# Create two lists of numbers to compare
list1 = [5.1, 5.1, 5.1]
list2 = [5.2, 5.1, 5.1]

# Define a function to check equality with tolerance
def assert_almost_equal(x, y, tol=1e-8):
    return np.abs(x - y) <= tol

# Check the equality of the 'value' attribute between nodes
assert assert_almost_equal(G.nodes[1]['value'], G.nodes[2]['value'])

# Check the equality of lists with tolerance
assert all(assert_almost_equal(x, y) for x, y in zip(list1, list2))
