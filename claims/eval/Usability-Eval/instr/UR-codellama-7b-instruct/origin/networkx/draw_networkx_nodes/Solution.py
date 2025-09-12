
import networkx as nx

# Generate a directed graph G with three nodes and one edge
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3])
G.add_edge(1, 2)

# Draw the nodes of the graph using the spring layout algorithm
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=5000)
