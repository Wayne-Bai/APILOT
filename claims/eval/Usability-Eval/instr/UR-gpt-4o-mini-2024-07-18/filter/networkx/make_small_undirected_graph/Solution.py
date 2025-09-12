import networkx as nx

def create_graph(graph_description):
    G = nx.Graph()
    for edge in graph_description:
        G.add_edge(edge[0], edge[1])
    return G

# Example usage:
graph_description = [(1, 2), (1, 3), (2, 4)]
graph = create_graph(graph_description)
