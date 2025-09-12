import networkx as nx

def find_communities_greedy_modularity(G):
    # Convert the graph to an undirected graph if it is not already
    if G.is_directed():
        G = G.to_undirected()
    
    # Initialize the partition with each node in its own community
    partition = [{node} for node in G.nodes()]
    
    # Initialize modularity
    modularity = nx.algorithms.community.modularity(G, partition)
    
    while True:
        best_increase = 0
        best_move = None
        
        for node in G.nodes():
            for community in partition:
                if node in community:
                    continue
                
                # Calculate the change in modularity if node is moved to community
                current_community = next(c for c in partition if node in c)
                new_partition = [c.copy() for c in partition]
                new_partition[new_partition.index(current_community)].remove(node)
                new_partition[new_partition.index(community)].add(node)
                
                new_modularity = nx.algorithms.community.modularity(G, new_partition)
                increase = new_modularity - modularity
                
                if increase > best_increase:
                    best_increase = increase
                    best_move = (node, community)
        
        if best_increase > 0:
            node, community = best_move
            current_community = next(c for c in partition if node in c)
            partition[partition.index(current_community)].remove(node)
            partition[partition.index(community)].add(node)
            modularity += best_increase
        else:
            break
    
    # Remove empty communities
    partition = [c for c in partition if c]
    
    return partition

# Example usage:
G = nx.karate_club_graph()
communities = find_communities_greedy_modularity(G)
print(communities)
