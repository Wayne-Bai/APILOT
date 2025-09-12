import networkx as nx

def find_communities(G):
    # Use the greedy_modularity_communities method
    communities = nx.algorithms.community.greedy_modularity_communities(G)
    return communities

# Sample usage:
G = nx.barabasi_albert_graph(100, 2)  # Generate a sample graph
communities = find_communities(G)
print(communities)
