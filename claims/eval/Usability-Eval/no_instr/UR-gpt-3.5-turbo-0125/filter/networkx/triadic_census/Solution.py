
import networkx as nx

def triadic_census_digraph(G, nodelist=None):
    if nodelist:
        G_sub = G.subgraph(nodelist)
    else:
        G_sub = G

    census = nx.triadic_census(G_sub)
    return census

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1,2), (1,3), (2,1), (3,1), (2,3)])

result = triadic_census_digraph(G)
print(result)
