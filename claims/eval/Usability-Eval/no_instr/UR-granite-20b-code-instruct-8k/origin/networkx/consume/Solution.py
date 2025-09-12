import networkx as nx

def consume_iterator_entirely(iterator):
    for _ in iterator:
        pass

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node(1)
G.add_nodes_from([2, 3, 4])
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (1, 4)])

# Iterate over the nodes and edges of the graph
consume_iterator_entirely(G.nodes())
consume_iterator_entirely(G.edges())
