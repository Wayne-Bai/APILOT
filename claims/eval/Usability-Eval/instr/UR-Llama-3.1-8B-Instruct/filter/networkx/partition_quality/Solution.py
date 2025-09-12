import networkx as nx
import np

def partition_coverage_performance(G, partition):
    """
    Returns the coverage and performance of a partition of G.

    Args:
    G (networkx graph): The input graph.
    partition (list): A list of vertex sets that partition the graph.

    Returns:
    tuple: A tuple containing the coverage and performance of the partition.
    """
    # Initialize variables to keep track of coverage and performance
    edge_count = 0
    subgraph_edges = 0

    # Iterate over each subgraph in the partition
    for subgraph in partition:
        # Create a subgraph consisting of the current partitioned vertices
        subgraph_G = G.subgraph(list(subgraph))
        
        # Count the number of edges in the subgraph
        subgraph_edges += subgraph_G.number_of_edges()
        
        # For each edge in the subgraph, check if it is also present in the original graph
        for edge in subgraph_G.edges():
            if G.has_edge(edge[0], edge[1]):
                edge_count += 1

    # Calculate coverage and performance
    coverage = edge_count / G.number_of_edges()
    performance = subgraph_edges / len(partition)

    return coverage * performance

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

    # Define a partition of the graph
    partition = [(1,), (2, 4), (3, 5)]

    # Calculate and print the coverage and performance
    coverage_performance = partition_coverage_performance(G, partition)
    print(f"Coverage and performance: {coverage_performance}")
