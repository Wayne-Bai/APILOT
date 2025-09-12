import networkx as nx

# create a sample graph
G = nx.gnm_random_graph(10, 20)

# define the harmonic centrality function
def harmonic_centrality(G):
    return sum([float(d[1]) / d[0] for n, d in G.nodes(data=True) if d[1] > 0]) / len(G.nodes())

# compute the harmonic centrality for each node
node_centralities = {n: harmonic_centrality(G[n]) for n in G}

# print the results
print(node_centralities)
