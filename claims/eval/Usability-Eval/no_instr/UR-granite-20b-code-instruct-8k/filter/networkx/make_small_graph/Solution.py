import networkx as nx

def return_small_graph(graph_description):
    """
    Returns the small graph described by graph_description.
    
    Parameters:
    graph_description (dict): A dictionary representing the graph.
    
    Returns:
    graph (nx.Graph): The small graph described by graph_description.
    """
    graph = nx.Graph()
    graph.add_nodes_from(graph_description.keys())
    for node, neighbors in graph_description.items():
        graph.add_edges_from([(node, neighbor) for neighbor in neighbors])
    return graph
