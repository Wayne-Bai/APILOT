
import networkx as nx

def generate_mixing_matrix(G, attribute):
    # Get the list of nodes and the attribute values
    nodes = list(G.nodes())
    values = [G.nodes[node][attribute] for node in nodes]

    # Create an empty mixing matrix
    mixing_matrix = {}

    # Calculate mixing parameter for each pair of values
    for i, value_i in enumerate(values):
        for j, value_j in enumerate(values):
            mixing_matrix[(value_i, value_j)] = 0

            for node in nodes:
                if G.nodes[node][attribute] == value_i:
                    for neighbor in G.neighbors(node):
                        if G.nodes[neighbor][attribute] == value_j:
                            mixing_matrix[(value_i, value_j)] += 1

            mixing_matrix[(value_i, value_j)] /= len(nodes)

    return mixing_matrix

# Example usage
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.nodes[1]['color'] = 'red'
G.nodes[2]['color'] = 'blue'
G.nodes[3]['color'] = 'red'
G.nodes[4]['color'] = 'blue'
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

mixing_matrix_color = generate_mixing_matrix(G, 'color')
print(mixing_matrix_color)
