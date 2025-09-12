import networkx as nx

def create_graph(graph_description):
    # Create an empty undirected graph
    G = nx.Graph()

    # Add nodes and edges based on the description
    for node, connections in graph_description.items():
        # Ensure the node is in the graph
        if node not in G:
            G.add_node(node)

        # Add edges between the node and its connections
        for connection in connections:
            G.add_edge(node, connection)

    return G

# Example description for a small graph
graph_description = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

# Create the graph
graph = create_graph(graph_description)

# Use NetworkX utility to visualize the graph (only for demonstration purpose)
# This part is optional and requires matplotlib
import matplotlib.pyplot as plt

nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=15)
plt.show()
