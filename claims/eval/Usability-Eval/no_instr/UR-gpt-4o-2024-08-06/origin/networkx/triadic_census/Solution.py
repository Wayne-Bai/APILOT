import networkx as nx

def triadic_census_of_graph(graph, nodelist=None):
    """
    Determines the triadic census of a directed graph.
    
    Parameters:
    graph (nx.DiGraph): A directed graph
    nodelist (list): A list of nodes to consider for triad census (optional)

    Returns:
    dict: A dictionary with keys as triad types and values as the count of each type
    """
    
    if nodelist is not None:
        # Create a subgraph with only the nodes in the nodelist
        subgraph = graph.subgraph(nodelist).copy()
    else:
        subgraph = graph

    # Calculate the triadic census
    triadic_census = nx.triadic_census(subgraph)
    
    return triadic_census

# Example usage:
# Create a directed graph
G = nx.DiGraph()
edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 1)]
G.add_edges_from(edges)

# Get the triadic census for the entire graph
census = triadic_census_of_graph(G)
print("Triadic Census:", census)

# Get the triadic census for a subgraph containing nodes 0, 1, and 2
nodelist = [0, 1, 2]
subcensus = triadic_census_of_graph(G, nodelist)
print("Subgraph Triadic Census:", subcensus)
