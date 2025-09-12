
import networkx as nx

def has_eulerian_path(G, source=None):
    """
    Returns True iff G has an Eulerian path. An Eulerian path is a path in a graph which uses each edge of a graph exactly once. If source is specified, then this function checks whether an Eulerian path that starts at node source exists.
    """
    # Check if the graph has any edges
    if not G.edges:
        return False

    # Check if the graph is connected
    if not nx.is_connected(G):
        return False

    # If source is specified, check if it exists in the graph
    if source is not None and source not in G:
        return False

    # Create a copy of the graph to perform BFS
    H = G.copy()

    # Perform BFS from the source node (if specified) or any arbitrary node in the graph
    if source is not None:
        start_node = source
    else:
        start_node = next(iter(H))
    visited = {start_node}
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        for neighbor in H[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Check if all nodes have been visited
    return len(visited) == nx.number_of_nodes(H)
