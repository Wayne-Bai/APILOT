import networkx as nx

def print_graph_info(G, n=None):
    """
    Prints a short summary of information for the graph G or the node n.
    
    Parameters:
    G (networkx graph): The graph object
    n (node): The node to print information about (optional)
    """
    if n is not None:
        # Print node information
        print("Node Information:")
        print(f"Degree: {G.degree(n)}")
        print(f"Neighbors: {list(G.neighbors(n))}")
    else:
        # Print graph information
        print("Graph Information:")
        print(f"Number of Nodes: {G.number_of_nodes()}")
        print(f"Number of Edges: {G.number_of_edges()}")
        print(f"Degree Centrality: {nx.degree_centrality(G)}")
        print(f"Clustering Coefficient: {nx.clustering(G)}")
        print(f"Density: {nx.density(G)}")

# Create an example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Print graph information
print_graph_info(G)

# Print node information
print_graph_info(G, 2)
