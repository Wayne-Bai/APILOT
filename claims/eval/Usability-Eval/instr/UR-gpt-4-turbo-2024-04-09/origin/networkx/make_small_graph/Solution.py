import networkx as nx

def create_graph_from_description(graph_description):
    G = nx.parse_graph6(graph_description)
    return G

# Example usage with a graph description in graph6 format
graph_description = "DQc"
small_graph = create_graph_from_description(graph_description)
print(nx.info(small_graph))
