import networkx as nx

def coverage(G, partition):
    # Ensure G is a graph with nodes and edges
    if not isinstance(G, nx.Graph):
        raise TypeError("G must be a NetworkX graph")
    if G.number_of_edges() == 0:
        return 0

    # Create a set for faster membership checking
    partition_sets = [set(part) for part in partition]

    intra_community_edges = 0

    # Count edges within the same partition
    for u, v in G.edges():
        for part_set in partition_sets:
            if u in part_set and v in part_set:
                intra_community_edges += 1
                break

    # Calculate coverage: intra-community edges divided by total edges
    total_edges = G.number_of_edges()
    coverage_value = intra_community_edges / total_edges

    return coverage_value

# Example usage
if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (0, 4), (1, 3)])
    partition = [{0, 1, 2}, {3, 4}]

    result = coverage(G, partition)
    print(f"Coverage of the partition: {result}")
