import networkx as nx

graph_description = "small undirected graph"

G = nx.Graph()

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

print(G.nodes())
print(G.edges())