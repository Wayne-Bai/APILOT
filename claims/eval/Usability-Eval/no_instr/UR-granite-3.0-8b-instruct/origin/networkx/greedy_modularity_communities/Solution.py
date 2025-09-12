import networkx as nx

def find_communities(G):
    # Create a community structure
    communities = {}

    # Initialize modularity
    modularity = 0

    # Iterate over each node in the graph
    for node in G.nodes():
        # Initialize community for the node
        community = node

        # Iterate over each neighbor of the node
        for neighbor in G.neighbors(node):
            # If neighbor is already in a community
            if neighbor in communities:
                # If modularity would increase if we merge the communities
                if modularity < nx.community.modularity(G, {node: community, neighbor: communities[neighbor]}):
                    # Merge the communities
                    communities[node] = community
                    communities[neighbor] = community
                    modularity = nx.community.modularity(G, communities)
                else:
                    # Keep the communities separate
                    pass
            else:
                # Add the neighbor to the community
                communities[neighbor] = community

        # Update modularity
        modularity = nx.community.modularity(G, communities)

    return communities

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 1)])

# Find communities
communities = find_communities(G)

# Print communities
for community, nodes in communities.items():
    print(f"Community {community}: {nodes}")
