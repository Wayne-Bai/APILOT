import networkx as nx

def calculate_partition(G, partition):
    """
    Returns the coverage and performance of a partition of G.
    
    Parameters:
    G (networkx.Graph): The graph.
    partition (list): A list of sets, each representing a partition.
    
    Returns:
    tuple: A tuple containing the coverage and performance of the partition.
    """
    
    # Initialize the coverage and performance measures
    coverage = 0
    performance = 0
    
    # Iterate over each subset in the partition
    for s in partition:
        # Check if the subset is a subgraph of G
        if nx.is_induced_subgraph(G, s):
            # Update the coverage measure
            coverage += len(s)
            
            # Calculate the performance measure (closeness) for the subset
            # This is done using the 'closeness_centrality' function from networkx
            performance += nx.closeness_centrality(G, subset=s)
    
    # Calculate the average performance of the partition
    avg_performance = performance / len(partition) if partition else 0
    
    # Return the coverage and average performance of the partition
    return coverage, avg_performance

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (5, 6)])

# Define a partition of the graph
partition = [nx.node_clique(G, i) for i in range(1, 7)]

# Calculate the coverage and average performance of the partition
coverage, avg_performance = calculate_partition(G, partition)

print("Coverage:", coverage)
print("Average Performance:", avg_performance)
