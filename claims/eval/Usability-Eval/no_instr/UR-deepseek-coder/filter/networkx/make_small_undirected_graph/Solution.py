import networkx as nx

def create_graph(graph_description):
    G = nx.Graph()
    
    for node in graph_description['nodes']:
        G.add_node(node)
    
    for edge in graph_description['edges']:
        G.add_edge(edge[0], edge[1])
    
    return G

# Example usage:
graph_description = {
    'nodes': [1, 2, 3, 4],
    'edges': [(1, 2), (2, 3), (3, 4), (4, 1)]
}

graph = create_graph(graph_description)
