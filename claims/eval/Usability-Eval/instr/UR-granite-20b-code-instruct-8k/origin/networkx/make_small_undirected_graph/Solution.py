import networkx as nx

graph_description = {
    "nodes": ["A", "B", "C", "D"],
    "edges": [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
}

G = nx.Graph()
G.add_nodes_from(graph_description["nodes"])
G.add_edges_from(graph_description["edges"])
