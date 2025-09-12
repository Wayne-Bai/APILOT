import networkx as nx

# Define the function to test Node Coverage of graph G
def node_coverage(G, partition):
    # Calculate the size of the union of all sets in the partition
    union_size = sum([len(nodes) for nodes in partition])
    # Calculate the total size of all nodes in G
    total_size = G.number_of_nodes()
    # Calculate the Node Coverage
    node_coverage = 1 - (union_size / total_size)
    return node_coverage

# Define the function to test Edge Coverage of graph G
def edge_coverage(G, partition):
    # Calculate the size of the union of all sets in the partition
    union_size = sum([len(edges) for nodes in partition for edges in G.edges(nodes)])
    # Calculate the total size of all edges in G
    total_size = G.number_of_edges()
    # Calculate the Edge Coverage
    edge_coverage = 1 - (union_size / total_size)
    return edge_coverage

# Define the function to test Performance of graph G
def performance(G, partition):
    # Calculate Edge Cut of the partition
    edge_cut = sum([G.degree(node) for nodes in partition for node in nodes])
    # Calculate Normalized Cut of the partition
    normalized_cut = 2 * edge_cut / (G.number_of_nodes()**2)
    # Calculate  Ratio Cut of the partition
    ratio_cut = sum([G.degree(node, weight='weight') for nodes in partition for node in nodes])
    # Calculate the Performance
    performance = (normalized_cut) + (ratio_cut / total_size)
    return performance
