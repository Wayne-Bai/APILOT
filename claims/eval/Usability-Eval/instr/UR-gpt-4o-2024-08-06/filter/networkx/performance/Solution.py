import networkx as nx

def performance(G, partition):
    """
    Calculate the performance of a partition of the graph.

    Parameters:
    G : NetworkX graph
        A networkx graph for which the performance is calculated.
        
    partition: list of sets
        Each set contains the nodes in one community.

    Returns:
    float
        The performance of the partition.
    """
    intra_edges = 0
    inter_non_edges = 0
    total_possible_edges = G.number_of_nodes() * (G.number_of_nodes() - 1) // 2

    node_to_community = {}
    for community, nodes in enumerate(partition):
        for node in nodes:
            node_to_community[node] = community

    for i, u in enumerate(G.nodes()):
        for j, v in enumerate(G.nodes()):
            if i < j:  # Consider each pair (u, v) once
                same_community = node_to_community[u] == node_to_community[v]
                if same_community and G.has_edge(u, v):
                    intra_edges += 1
                elif not same_community and not G.has_edge(u, v):
                    inter_non_edges += 1

    return (intra_edges + inter_non_edges) / total_possible_edges

# Example of usage:

# Create a simple graph
G = nx.erdos_renyi_graph(10, 0.3)

# Define a simple partition
partition = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8, 9}]

# Calculate performance
perf = performance(G, partition)
print(f"The performance of the partition is: {perf}")
