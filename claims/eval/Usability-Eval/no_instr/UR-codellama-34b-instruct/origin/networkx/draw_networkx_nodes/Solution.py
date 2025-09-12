
import networkx as nx

# create an empty graph
G = nx.Graph()

# add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])

# draw the nodes of the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1000, alpha=0.8, node_color='skyblue', cmap=plt.cm.Blues)
nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

plt.axis('off')
plt.show()
