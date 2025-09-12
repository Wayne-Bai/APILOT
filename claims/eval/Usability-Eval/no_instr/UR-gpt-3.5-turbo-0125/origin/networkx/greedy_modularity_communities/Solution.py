
import networkx as nx

G = nx.Graph()

# Add nodes and edges to the graph G

communities = nx.algorithms.community.greedy_modularity_communities(G)
