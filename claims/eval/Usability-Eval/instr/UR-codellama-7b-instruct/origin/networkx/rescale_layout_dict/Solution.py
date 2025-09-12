
import networkx as nx

# create a sample graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

# calculate the scaled positions for each node in the graph
positions = nx.spring_layout(G, k=1, n_iter=50)

# create a dictionary of scaled positions keyed by node
scaled_positions = {node: position for node, position in positions.items()}
