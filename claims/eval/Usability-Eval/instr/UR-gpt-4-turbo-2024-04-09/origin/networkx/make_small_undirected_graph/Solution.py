import networkx as nx

def create_graph():
    # Create an empty undirected graph
    G = nx.Graph()

    # Add nodes
    # For example, adding node 1 to node 5
    G.add_nodes_from([1, 2, 3, 4, 5])

    # Add edges
    # For example, adding some edges between the nodes
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)]
    G.add_edges_from(edges)
    
    return G

# Create the graph
graph = create_graph()

# Print the nodes and edges to see the graph structure
print("Nodes in the graph:", graph.nodes())
print("Edges in the graph:", graph.edges())
