import networkx as nx

def quotient_graph(G, partition):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.
    
    Parameters:
    G : NetworkX Graph
        An input graph.
    
    partition : list of sets
        The partition of the graph's node set, where each set is a group of equivalent nodes.

    Returns:
    Q : NetworkX Graph
        The quotient graph.
    """
    Q = nx.Graph()
    
    # Add nodes for each set in the partition
    for i, subset in enumerate(partition):
        Q.add_node(i)
    
    # Create a mapping from original nodes to subsets
    node_to_subset = {}
    for subset_index, subset in enumerate(partition):
        for node in subset:
            node_to_subset[node] = subset_index
    
    # Iterate over the edges of the original graph and add
    # edges between subsets to the quotient graph
    for u, v in G.edges():
        u_subset = node_to_subset[u]
        v_subset = node_to_subset[v]
        
        # Add an edge between two nodes only if they belong to different subsets
        if u_subset != v_subset:
            Q.add_edge(u_subset, v_subset)
    
    return Q

# Example of usage
if __name__ == "__main__":
    # Create a graph
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (3, 4), (4, 5), (1, 5)])
    
    # Define a partition of the node set
    partition = [{0, 1, 2}, {3, 4, 5}]
    
    # Get the quotient graph
    Q = quotient_graph(G, partition)
    
    # Print the edges of the quotient graph
    print("Edges in the quotient graph:", Q.edges())
