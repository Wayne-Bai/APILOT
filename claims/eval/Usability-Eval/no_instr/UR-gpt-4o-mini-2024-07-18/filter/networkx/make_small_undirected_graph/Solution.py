import networkx as nx

def create_graph(graph_description):
    G = nx.Graph()
    for node in graph_description['nodes']:
        G.add_node(node)
    for edge in graph_description['edges']:
        G.add_edge(edge[0], edge[1])
    return G

# Example graph description
graph_description = {
    'nodes': ['A', 'B', 'C', 'D'],
    'edges': [('A', 'B'), ('A', 'C'), ('B', 'D')]
}

graph = create_graph(graph_description)
print(graph.nodes())
print(graph.edges())
