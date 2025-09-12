
import networkx as nx

def triadic_census(G, nodelist=None):
    if nodelist:
        subgraph = G.subgraph(nodelist)
    else:
        subgraph = G

    census = [0] * 16
    for node in subgraph.nodes():
        neighbors = set(subgraph.neighbors(node))
        for u, v in nx.combinations(neighbors, 2):
            if subgraph.has_edge(u, v) and subgraph.has_edge(v, u):
                if subgraph.has_edge(node, u) and subgraph.has_edge(u, node) and subgraph.has_edge(node, v) and subgraph.has_edge(v, node):
                    census[0] += 1  # type 1: mutual triangles
                elif subgraph.has_edge(node, u) and subgraph.has_edge(u, node) and subgraph.has_edge(v, node):
                    census[1] += 1  # type 2: asymmetric unidirectional triangles
                elif subgraph.has_edge(node, v) and subgraph.has_edge(v, node) and subgraph.has_edge(u, node):
                    census[2] += 1  # type 3: asymmetric bidirectional triangles
                else:
                    census[3] += 1  # type 4: mutual dyads
            elif subgraph.has_edge(u, v):
                if subgraph.has_edge(node, u) and subgraph.has_edge(node, v):
                    census[4] += 1  # type 5: asymmetric digraph types I
                elif subgraph.has_edge(node, u):
                    census[5] += 1  # type 6: asymmetric digraph types II
                elif subgraph.has_edge(node, v):
                    census[6] += 1  # type 7: asymmetric digraph types III
                else:
                    census[7] += 1  # type 8: asymmetric non-dyads
            elif subgraph.has_edge(v, u):
                if subgraph.has_edge(node, u) and subgraph.has_edge(node, v):
                    census[8] += 1  # type 9: asymmetric digraph types IV
                elif subgraph.has_edge(node, u):
                    census[9] += 1  # type 10: asymmetric digraph types V
                elif subgraph.has_edge(node, v):
                    census[10] += 1  # type 11: asymmetric digraph types VI
                else:
                    census[11] += 1  # type 12: asymmetric digraph types VII
            else:
                if subgraph.has_edge(node, u) and subgraph.has_edge(node, v):
                    census[12] += 1  # type 13: asymmetric non-transitives
                elif subgraph.has_edge(node, u) or subgraph.has_edge(node, v):
                    census[13] += 1  # type 14: asymmetric non-receivers
                else:
                    census[14] += 1  # type 15: asymmetric non-senders
    census[15] += nx.number_of_isolates(subgraph)  # type 16: isolated nodes

    return census
