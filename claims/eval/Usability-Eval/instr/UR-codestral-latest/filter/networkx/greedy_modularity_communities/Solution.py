import networkx as nx

# Assuming you have your graph defined as G

# The function to find communities
def find_communities(G):
    # Convert the graph to undirected if it's not
    G = nx.Graph(G)

    # Use the greedy_modularity_communities function from networkx.community, which is the updated version
    communities = nx.community.greedy_modularity_communities(G)

    # Return the communities
    return communities

# Assign the return value from function to communities
communities = find_communities(G)

# Print the communities
for i, community in enumerate(communities):
    print(f"Community {i}: {community}")
