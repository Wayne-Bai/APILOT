# Import necessary libraries
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add some nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Draw the nodes of the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_shape="s", node_color='lightblue')
plt.show()

# To run the above code, matplotlib needs to be installed.
# You can install it by using the pip install matplotlib command.
