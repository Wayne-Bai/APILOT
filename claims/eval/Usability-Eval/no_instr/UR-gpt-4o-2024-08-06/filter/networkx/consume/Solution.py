import networkx as nx

def consume_iterator(iterator):
    """Consume an iterator entirely, discarding all values."""
    # Using the built-in collections.deque with a maxlen of 0 to efficiently consume an iterator
    from collections import deque
    deque(iterator, maxlen=0)

# Example usage
# Create a sample networkx graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Get an iterator of nodes
node_iterator = iter(G.nodes)

# Consume the iterator
consume_iterator(node_iterator)
