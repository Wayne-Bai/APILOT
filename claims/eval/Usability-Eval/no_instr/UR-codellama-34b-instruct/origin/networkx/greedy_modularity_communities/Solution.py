
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])

# Compute the modularity of the graph
modularity = nx.community.modularity(G, G.nodes())

# Print the initial modularity of the graph
print("Initial modularity:", modularity)

# Find communities in the graph using greedy modularity maximization
communities = nx.community.greedy_modularity_maximization(G, G.nodes())

# Print the final modularity of the graph and the number of communities found
print("Final modularity:", modularity)
print("Number of communities:", len(communities))
