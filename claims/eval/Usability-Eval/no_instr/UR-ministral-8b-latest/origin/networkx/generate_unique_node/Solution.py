import networkx as nx
import random

# Function to generate a unique node label
def generate_unique_node_label():
    while True:
        label = 'node_{}'.format(random.randint(1, 10000))
        if label not in graph.nodes():
            return label

# Example usage
G = nx.Graph()

# Adding unique node labels
for i in range(1, 11):
    G.add_node(generate_unique_node_label())

print(G.nodes())
