import networkx as nx

# Function to check if G has an Eulerian path
def eulerian_path_exists(G, source=None):
    degree_sequence = dict(G.degree())

    # Check if there is an even number of nodes with odd degree
    odd_degree_nodes = [node for node, degree in degree_sequence.items() if degree % 2 != 0]

    if len(odd_degree_nodes) > 2:
        return False

    if len(odd_degree_nodes) == 2:
        # Add an edge to connect the two odd degree nodes
        return G.add_edge(odd_degree_nodes[0], odd_degree_nodes[1])

    # Eulerian path exists if there's no need to add any edge
    return True

# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
print(eulerian_path_exists(G))  # True or False
