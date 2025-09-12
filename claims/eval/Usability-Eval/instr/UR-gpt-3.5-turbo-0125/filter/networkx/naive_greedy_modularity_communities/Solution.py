
import networkx as nx

G = nx.Graph()

# Add nodes and edges to the graph G

communities_generator = nx.community.greedy_modularity_communities(G)
communities = list(communities_generator)

print(communities)
