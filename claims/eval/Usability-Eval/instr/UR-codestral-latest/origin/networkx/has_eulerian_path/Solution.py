import networkx as nx

def has_eulerian_path(G, source=None):
    # Check if the graph is connected
    if not nx.is_connected(G):
        return False

    # Count the degree of each node
    degrees = dict(G.degree())

    # Count the nodes with odd degree
    odd_degree_nodes = [node for node, degree in degrees.items() if degree % 2 != 0]

    # If there are no or exactly two nodes with odd degree
    if len(odd_degree_nodes) == 0 or len(odd_degree_nodes) == 2:
        # If source is specified
        if source is not None:
            # If there are no nodes with odd degree, any node can be the source
            # If there are two nodes with odd degree, they have to be the source and the end of the path
            return (len(odd_degree_nodes) == 0) or (odd_degree_nodes[0] == source and odd_degree_nodes[1] != source)
        else:
            return True
    else:
        return False
