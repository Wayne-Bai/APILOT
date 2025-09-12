
import networkx as nx

def mixing_matrix(G, attribute):
    # Get the node attributes
    node_attributes = nx.get_node_attributes(G, attribute)
    
    # Initialize the mixing matrix
    mixing_matrix = {}
    
    # Calculate the mixing matrix values
    for node in G.nodes():
        mixing_matrix[node] = {}
        for neighbor in G.neighbors(node):
            if node_attributes[node] not in mixing_matrix[node]:
                mixing_matrix[node][node_attributes[node]] = {}
            mixing_matrix[node][node_attributes[node]][node_attributes[neighbor]] = mixing_matrix[node][node_attributes[node]].get(node_attributes[neighbor], 0) + 1
    
    return mixing_matrix

# Example usage
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
nx.set_node_attributes(G, {1: 'A', 2: 'B', 3: 'A', 4: 'B'}, 'color')

mixing = mixing_matrix(G, 'color')
print(mixing)
