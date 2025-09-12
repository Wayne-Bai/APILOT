import networkx as nx

# Define the function for finding communities using greedy modularity maximization
def find_communities(G):
    # Compute the initial modularity score
    Q_init = nx.modularity_max(G)
    
    # Find the maximum modularity score by iteratively removing nodes and computing the modularity score for each iteration
    max_Q = 0
    for node in G:
        H = G.subgraph([node])
        Q = nx.modularity_max(H)
        if Q > max_Q:
            max_Q = Q
    
    # Return the community of nodes that maximizes the modularity score
    return [node for node in G if nx.find_cliques(G)]

# Use the function to find communities in a graph
G = nx.gnm_random_graph(10, 20)
communities = find_communities(G)
print("Communities:", communities)