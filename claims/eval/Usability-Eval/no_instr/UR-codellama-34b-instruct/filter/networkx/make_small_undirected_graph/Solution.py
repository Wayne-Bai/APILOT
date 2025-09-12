
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C'])

# Add edges between nodes
G.add_edges_from([('A', 'B'), ('B', 'C')])
