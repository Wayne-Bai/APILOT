import networkx as nx

def create_graph(graph_description):
    G = nx.Graph()
    for node, neighbors in graph_description.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G

# Example usage:
graph_description = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

graph = create_graph(graph_description)
print(graph.edges())
