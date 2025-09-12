import networkx as nx

# create a directed graph
G = nx.DiGraph()

# add edges with weight
edges = [("A", "B", 0.5), ("B", "C", 0.5), ("C", "A", 1.0)]
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# compute PageRank with the weighted edges
pagerank = nx.pagerank(G, weight='weight')

print("PageRank scores:", pagerank)
