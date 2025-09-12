import networkx as nx

def create_graph_by_description(graph_description):
    G = nx.Graph()   # Creating an undirected graph
    # Assuming graph_description is a list of tuples (node1, node2)
    for node1, node2 in graph_description:
        G.add_edge(node1, node2)
    return G

# Example usage:
graph_description = [(1, 2), (2, 3), (3, 1), (1, 4)]
G = create_graph_by_description(graph_description)
print("Nodes in the graph:", G.nodes())
print("Edges in the graph:", G.edges())
