import networkx as nx

def consume_iterator(iterator):
    """
    Consume the iterator entirely.
    
    :param iterator: The input iterator to be consumed.
    """
    for _ in iterator:
        pass

# Create a directed Graph
G = nx.DiGraph()

# Add edges to the Graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'A')

# Create a depth-first search iterator
dfs_iterator = nx.dfs_postorder_nodes(G)

# Consume the iterator entirely
consume_iterator(dfs_iterator)

# Create neighbors iterator for node 'A'
neighbors_iterator = G.neighbors('A')

# Consume the iterator entirely
consume_iterator(neighbors_iterator)

# Create edges iterator
edges_iterator = G.edges()

# Consume the iterator entirely
consume_iterator(edges_iterator)
