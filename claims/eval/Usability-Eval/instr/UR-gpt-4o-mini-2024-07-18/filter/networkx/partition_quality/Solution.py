import networkx as nx

def evaluate_partition(G, partition):
    """
    Returns the coverage and performance of a partition of G.
    
    Parameters:
    G (networkx.Graph): The graph to evaluate.
    partition (list of lists): A partition of the graph G, 
                                where each sublist represents a set of nodes.

    Returns:
    tuple: A tuple containing the coverage and performance of the partition.
    """
    
    # Initialize coverage and performance
    coverage = 0
    performance = 0
    
    # Get total number of edges in the graph
    total_edges = G.number_of_edges()
    
    for community in partition:
        # Check if the community is non-empty
        if not community:
            continue

        # Create a subgraph induced by the community
        subgraph = G.subgraph(community)
        
        # Calculate the number of edges within the community
        internal_edges = subgraph.number_of_edges()
        
        # Calculate coverage as the proportion of internal edges
        coverage += internal_edges / total_edges if total_edges > 0 else 0
        
        # Calculate performance as a measure of internal connectivity
        # Here we simply use internal edges
        performance += internal_edges

    # Normalize coverage by the number of communities
    coverage /= len(partition) if partition else 1
    
    return coverage, performance

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5)])

    # Define a partition of the graph
    partition = [[1, 2, 3], [4, 5]]

    # Evaluate the partition
    coverage, performance = evaluate_partition(G, partition)
    print("Coverage:", coverage)
    print("Performance:", performance)
