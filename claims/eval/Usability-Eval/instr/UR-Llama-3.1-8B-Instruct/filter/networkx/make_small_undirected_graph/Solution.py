import networkx as nx
import matplotlib.pyplot as plt

# Define the graph description
graph_description = {
    "nodes": ["A", "B", "C", "D", "E"],
    "edges": [
        ["A", "B"],
        ["B", "C"],
        ["C", "D"],
        ["D", "E"],
        ["A", "E"],
        ["A", "C"]
    ]
}

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(graph_description["nodes"])

# Add edges to the graph
G.add_edges_from(graph_description["edges"])

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
