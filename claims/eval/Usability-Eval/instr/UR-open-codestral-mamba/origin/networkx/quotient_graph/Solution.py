import networkx as nx

def create_quotient_graph(G, equivalence_relation):
    quotient_graph = nx.Graph()
    equivalence_classes = equivalence_relation(G.nodes())
    for eq_class in equivalence_classes:
        quotient_graph.add_node(frozenset(eq_class))
    for u in G.nodes():
        for v in G.nodes():
            if u == v or not equivalence_relation(u, v):
                continue
            if quotient_graph.has_edge(frozenset(u), frozenset(v)):
                quotient_graph.add_edge(frozenset(u), frozenset(v), weight=G[u][v].get('weight', 1))
            else:
                quotient_graph.add_edge(frozenset(u), frozenset(v), weight=0)
    for u, v in G.edges():
        if not quotient_graph.has_edge(frozenset(u), frozenset(v)):
            quotient_graph.add_edge(frozenset(u), frozenset(v), weight=0)
    return quotient_graph
