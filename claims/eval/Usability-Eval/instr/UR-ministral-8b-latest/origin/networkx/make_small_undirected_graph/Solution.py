import networkx as nx
import matplotlib.pyplot as plt

def create_graph(graph_description):
    # Example input format for graph_description: "A-B"
    # where 'A' and 'B' are nodes connected by an edge

    edges = graph_description.split('-')
    G = nx.Graph()

    # Adding edges between nodes
    for i in range(0, len(edges), 2):
        if i < len(edges) - 1:
            G.add_edge(edges[i], edges[i + 1])

    return G

# Example usage
graph_description = "A-B"
graph = create_graph(graph_description)

# Plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
