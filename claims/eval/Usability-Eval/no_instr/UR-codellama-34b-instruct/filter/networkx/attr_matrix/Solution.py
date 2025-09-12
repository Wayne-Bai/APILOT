
import networkx as nx

def get_attribute_matrix(G):
    # Get the list of nodes in the graph
    nodes = list(G.nodes())
    # Create a numpy array to store the attribute values
    attr_array = np.zeros((len(nodes), len(nodes)), dtype=np.float32)

    # Iterate over each node and its neighbors
    for i, node in enumerate(nodes):
        # Get the list of neighboring nodes
        neighbors = G.neighbors(node)
        # Iterate over each neighbor and calculate the attribute value
        for j, neighbor in enumerate(neighbors):
            attr_array[i][j] = G.edges[node, neighbor]['weight']

    return attr_array
