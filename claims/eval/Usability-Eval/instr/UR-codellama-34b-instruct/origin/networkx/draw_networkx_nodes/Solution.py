
import networkx as nx

# Define the graph G
G = nx.Graph()

# Add nodes to the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Draw the nodes of the graph G
pos = nx.spring_layout(G, k=0.5)
nx.draw_networkx_nodes(G, pos, node_size=5000, node_color='lightblue', cmap=plt.get_cmap('Blues'))

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')

# Draw the edges of the graph G
nx.draw_networkx_edges(G, pos, width=1.0, edge_color='gray')

# Show the plot
plt.show()
