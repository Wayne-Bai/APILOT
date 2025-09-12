import networkx as nx

def shortest_path_lengths_to_target(G, target):
    # Calculate the shortest path lengths from all nodes to the target node
    lengths = nx.shortest_path_length(G, target=target)
    return lengths
