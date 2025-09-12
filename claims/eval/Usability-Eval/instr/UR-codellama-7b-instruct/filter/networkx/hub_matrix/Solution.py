import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)

# Compute the HITS hub matrix
hub_matrix = nx.hits(G)

print("Hub matrix:")
for i in range(len(hub_matrix)):
    print(f"Hub {i}: {hub_matrix[i]}")
