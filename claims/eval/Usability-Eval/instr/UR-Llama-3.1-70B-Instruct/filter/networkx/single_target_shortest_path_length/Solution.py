import networkx as nx
import matplotlib.pyplot as plt

def compute_shortest_paths(G, target):
    """
    Compute the shortest path lengths to target from all reachable nodes.
    
    Parameters:
    G (nx.Graph): The input graph.
    target (node): The target node.
    
    Returns:
    dict: A dictionary with nodes as keys and their shortest path lengths to the target as values.
    """
    # Initialize a dictionary to store the shortest path lengths
    shortest_paths = {}
    
    # Use the single-source shortest path length function from NetworkX
    for node in G.nodes:
        try:
            shortest_paths[node] = nx.shortest_path_length(G, source=node, target=target)
        except nx.NetworkXNoPath:
            # If there's no path from the node to the target, set the path length to infinity
            shortest_paths[node] = float('inf')
    
    return shortest_paths

# Example usage:
# Create a new graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (4, 5)])

# Compute the shortest path lengths to the target node (5)
target_node = 5
shortest_path_lengths = compute_shortest_paths(G, target_node)

print("Shortest path lengths to node", target_node, "from all reachable nodes:")
for node, path_length in shortest_path_lengths.items():
    print(f"Node {node}: {path_length}")

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='gray')
plt.show()
