import networkx as nx

def consume_iterator(iterator):
    # Consume the iterator entirely by converting it into a list
    consumed_list = list(iterator)
    return consumed_list

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')

# Use the iterator returned by nodes() or edges() method
nodes_iterator = G.nodes()
edges_iterator = G.edges()

# Consume the iterators entirely
consumed_nodes = consume_iterator(nodes_iterator)
consumed_edges = consume_iterator(edges_iterator)

# Print the consumed nodes and edges
print("Consumed Nodes: ", consumed_nodes)
print("Consumed Edges: ", consumed_edges)

# Alternatively, you can directly convert the iterators into lists without using a separate function
consumed_nodes_direct = list(G.nodes())
consumed_edges_direct = list(G.edges())

# Print the consumed nodes and edges
print("Consumed Nodes (Direct): ", consumed_nodes_direct)
print("Consumed Edges (Direct): ", consumed_edges_direct)
