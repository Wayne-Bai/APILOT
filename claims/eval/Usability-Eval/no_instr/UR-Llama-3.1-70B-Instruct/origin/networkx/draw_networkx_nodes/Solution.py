import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "A")
G.add_edge("A", "C")

# Draw the nodes of the graph
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), node_size=500, node_color='lightblue')

# Draw the edges of the graph
nx.draw_networkx_edges(G, pos=nx.spring_layout(G), width=2, edge_color='gray')

# Draw the labels of the nodes
nx.draw_networkx_labels(G, pos=nx.spring_layout(G))

# Show the plot
plt.axis('off')
plt.show()
