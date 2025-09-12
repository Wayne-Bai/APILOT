
import networkx as nx

# Define the graph G
G = nx.gnp_random_graph(100, 0.1)

# Find communities using greedy modularity maximization
communities = nx.community.greedy_modularity_communities(G)
