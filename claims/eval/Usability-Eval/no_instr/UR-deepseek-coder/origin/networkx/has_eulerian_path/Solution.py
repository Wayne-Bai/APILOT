import networkx as nx

def has_eulerian_path(G, source=None):
    # Check if the graph is connected
    if not nx.is_connected(G):
        return False
    
    # Count the degree of each node
    in_degrees = dict(G.in_degree())
    out_degrees = dict(G.out_degree())
    
    # If source is specified, check if it has out_degree = in_degree + 1
    if source is not None:
        if out_degrees[source] != in_degrees[source] + 1:
            return False
    
    # Count nodes with in_degree != out_degree
    start_nodes = 0
    end_nodes = 0
    
    for node in G.nodes():
        if out_degrees[node] - in_degrees[node] == 1:
            start_nodes += 1
            if start_nodes > 1:
                return False
        elif in_degrees[node] - out_degrees[node] == 1:
            end_nodes += 1
            if end_nodes > 1:
                return False
        elif in_degrees[node] != out_degrees[node]:
            return False
    
    # If there is exactly one start node and one end node, or all nodes have equal in and out degrees
    return (start_nodes == 1 and end_nodes == 1) or (start_nodes == 0 and end_nodes == 0)

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# print(has_eulerian_path(G))  # Output: True
