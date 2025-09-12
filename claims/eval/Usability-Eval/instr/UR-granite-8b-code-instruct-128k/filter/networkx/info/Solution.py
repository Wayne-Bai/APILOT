import networkx as nx

# Assuming you have already created a graph G
G = nx.Graph()

# To print a short summary of information for the graph G
print(nx.info(G))

# To print a short summary of information for a specific node n in the graph G
n = 1
print(nx.info(G, n))
