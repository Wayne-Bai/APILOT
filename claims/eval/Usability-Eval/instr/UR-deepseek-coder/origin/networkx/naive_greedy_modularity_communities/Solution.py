import networkx as nx

def find_communities_greedy_modularity(G):
    # Convert the graph to undirected if it is not already
    if G.is_directed():
        G = G.to_undirected()
    
    # Initialize the partition with each node in its own community
    partition = [{node} for node in G.nodes()]
    
    # Initialize modularity
    modularity = nx.algorithms.community.modularity(G, partition)
    
    # Iterate until no improvement in modularity
    while True:
        best_modularity = modularity
        best_partition = partition
        
        # Try merging each pair of communities
        for i in range(len(partition)):
            for j in range(i + 1, len(partition)):
                # Merge communities i and j
                new_partition = partition[:i] + partition[i+1:j] + partition[j+1:] + [partition[i] | partition[j]]
                
                # Calculate new modularity
                new_modularity = nx.algorithms.community.modularity(G, new_partition)
                
                # Update best partition if modularity improves
                if new_modularity > best_modularity:
                    best_modularity = new_modularity
                    best_partition = new_partition
        
        # If no improvement, break the loop
        if best_modularity == modularity:
            break
        
        # Update partition and modularity
        partition = best_partition
        modularity = best_modularity
    
    return partition

# Example usage:
# G = nx.karate_club_graph()
# communities = find_communities_greedy_modularity(G)
# print(communities)
