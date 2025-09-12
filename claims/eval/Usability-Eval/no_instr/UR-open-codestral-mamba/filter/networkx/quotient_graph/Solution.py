import networkx as nx

def generate_quotient_graph(G, equivalence_relation):
    quotient_graph = nx.Graph()
    for node in G.nodes():
        quotient_graph.add_node(node, attr_dict=G.nodes[node])
    for u, v, attr in G.edges(data=True):
        if equivalence_relation(u, v):
            if quotient_graph.has_edge(u, v):
                quotient_graph[u][v]['attr_dict'] += [attr]
            else:
                quotient_graph.add_edge(u, v, attr_dict=[attr])
    return quotient_graph
