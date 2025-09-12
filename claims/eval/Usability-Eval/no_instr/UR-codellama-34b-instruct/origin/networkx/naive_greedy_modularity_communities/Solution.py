
import networkx as nx

# Generate a random graph G
G = nx.gnp_random_graph(100, 0.5)

# Define the partition of the nodes into communities
partition = {node: int(node % 2 == 0) for node in G.nodes()}

# Calculate the modularity of the partition using the NetworkX API
modularity = nx.community.modularity(G, partition)

# Print the modularity value
print("Modularity:", modularity)
