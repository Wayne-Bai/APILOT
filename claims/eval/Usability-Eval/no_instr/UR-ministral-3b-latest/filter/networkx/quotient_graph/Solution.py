import networkx as nx

def get_quotient_graph(G, relation):
    # Create the quotient graph
    quotient_graph = nx.Graph()

    # Create an arbitrary node in the quotient graph
    quotient_graph.add_node(tuple(G.relationship_nodes(relation)))

    for u, v in G.edge_iter():
        if relation(u, v):
            quotient_graph.add_edge(tuple(G.relationship_nodes(relation)))

    return quotient_graph

# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])

relation = lambda x, y: x == y % 2
quotient_graph = get_quotient_graph(G, relation)

print(f"Quotient graph edges: {list(quotient_graph.edges())}")
