import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes (optional)
# G.add_node('a')
# G.add_node('b')

# Add edges (optional)
# G.add_edge('a', 'b')
# G.add_edge('b', 'c')

# Draw nodes
nodelist = nx.nodes(G)
pos = nx.spring_layout(G)  # positions for all nodes

nx.draw_nodes(G, pos, node_color='blue', node_size=200)
nx.draw_networkx_nodes(G, pos)

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='green', arrows=False)

plt.show()
