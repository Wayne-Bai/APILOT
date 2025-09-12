
import networkx as nx

# Create a graph G

# Find communities in G using greedy modularity maximization
communities_generator = nx.community.greedy_modularity_communities(G)

communities = []
for c in communities_generator:
    communities.append(list(c))

print(communities)
