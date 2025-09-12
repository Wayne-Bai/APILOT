import networkx as nx

def create_prefix_tree(paths):
    # Create a directed graph
    graph = nx.DiGraph()

    # Iterate over each path in the list of paths
    for path in paths:
        # Iterate over each node in the path
        for i in range(len(path)):
            # Add nodes and edges for each prefix in the path
            if i == 0:
                # Check if the root node exists; if not add it
                if not graph.has_node(path[0]):
                    graph.add_node(path[0])
            else:
                # Add edge from previous node to current node if it doesn't already exist
                if not graph.has_edge(path[i-1], path[i]):
                    graph.add_edge(path[i-1], path[i])

            # Always ensure current node is in the graph (important for leaf nodes)
            if not graph.has_node(path[i]):
                graph.add_node(path[i])

    return graph

# Example usage
paths = [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'e']]
prefix_tree = create_prefix_tree(paths)
print("Nodes:", prefix_tree.nodes())
print("Edges:", prefix_tree.edges())
