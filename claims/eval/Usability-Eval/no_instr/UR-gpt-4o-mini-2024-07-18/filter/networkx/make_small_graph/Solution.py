import networkx as nx

def create_graph(graph_description):
    G = nx.Graph()
    
    # Assuming graph_description is a list of edges
    for edge in graph_description:
        G.add_edge(edge[0], edge[1])
    
    return G

# Example usage
graph_description = [(1, 2), (2, 3), (3, 1)]
graph = create_graph(graph_description)
