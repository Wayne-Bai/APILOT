import networkx as nx

# Create an instance of a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edges_from([(1, 2), (2, 3), (1, 3)])

# Greedy Modularity Maximization to find communities
partition = nx.algorithms.community.greedy_modularity_communities(G)

print("Communities:")
for community in partition:
    print(community)
