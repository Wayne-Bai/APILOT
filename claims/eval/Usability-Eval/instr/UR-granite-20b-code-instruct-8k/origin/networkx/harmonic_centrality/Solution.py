import networkx as nx

# create an empty graph
G = nx.Graph()

# add edges to the graph
G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)])

# compute harmonic centrality for nodes
harmonic_centrality = nx.harmonic_centrality(G)

# print the harmonic centrality scores
for node, score in harmonic_centrality.items():
    print(f"Node {node} has a harmonic centrality score of {score:.3f}")
