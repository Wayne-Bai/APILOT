import networkx as nx

# Define the graph
G = nx.Graph()

# Add nodes to the graph with attributes
G.add_node(1, color='red')
G.add_node(2, color='blue')

# Define the mixing matrix
mixing_matrix = {
    (1, 2): 0.5,
    (2, 1): 0.5
}

# Assign the mixing matrix as edge weights
for edge, weight in mixing_matrix.items():
    G.add_edge(*edge, weight=weight)

# Define a function to calculate the attribute mixing matrix
def calculate_attribute_mixing_matrix(graph):
    attribute_mixing_matrix = {}
    for node in graph.nodes():
        neighbors = graph.neighbors(node)
        attribute_counts = {}
        for neighbor in neighbors:
            attribute = graph.nodes[neighbor]['color']
            if attribute in attribute_counts:
                attribute_counts[attribute] += 1
            else:
                attribute_counts[attribute] = 1
        total_neighbors = len(neighbors)
        for attribute, count in attribute_counts.items():
            attribute_mixing_matrix[(node, attribute)] = count / total_neighbors
    return attribute_mixing_matrix

# Calculate the attribute mixing matrix
attribute_mixing_matrix = calculate_attribute_mixing_matrix(G)

# Print the attribute mixing matrix
for (node, attribute), weight in attribute_mixing_matrix.items():
    print(f"Mixing matrix for attribute {attribute} of node {node}: {weight}")
