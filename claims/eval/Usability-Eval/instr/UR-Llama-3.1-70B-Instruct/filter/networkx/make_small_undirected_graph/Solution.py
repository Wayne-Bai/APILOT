import networkx as nx

def create_small_undirected_graph():
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 1)
    G.add_edge(1, 4)
    G.add_edge(2, 4)

    return G

graph_description = create_small_undirected_graph()

print("Nodes: ", graph_description.nodes())
print("Edges: ", graph_description.edges())
print("Degree: ", dict(graph_description.degree()))
print("Is Connected: ", nx.is_connected(graph_description))
print("Is Cyclic: ", not nx.is_directed_acyclic_graph(graph_description.to_directed()))
