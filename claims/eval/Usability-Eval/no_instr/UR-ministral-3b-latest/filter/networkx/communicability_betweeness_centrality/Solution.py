import networkx as nx
G = nx.erdos_renyi_graph(50, 0.4)
communicability_matrix = nx.communicability_matrix(G)
print(communicability_matrix)