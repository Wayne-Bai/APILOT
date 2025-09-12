import networkx as nx
import itertools

# Create a sample directed graph
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])

# Function to consume the iterator entirely
def consume_iterator(iterator):
    try:
        for item in iterator:
            yield item
    except StopIteration:
        pass

# Consume the edges of the graph
edges = list(G.edges)  # Get all edges in the graph
print('Original edges:', edges)
edges_iterator = iter(edges)  # Create an iterator for the edges
consumed_edges = list(consume_iterator(edges_iterator))
print('Consumed edges:', consumed_edges)

# Another example using itertools for a complete iteration
all_nodes = list(nx.nodes(G))
all_edges = list(nx.edges(G))
all_edges_iter = itertools.islice(all_edges, None)  # Create an iterator for all edges
consumed_all_edges = list(consume_iterator(all_edges_iter))
print('Consumed all edges using itertools.islice:', consumed_all_edges)
