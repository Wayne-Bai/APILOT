
import networkx as nx

# Define a list of nodes and edges in the form of tuples
nodes = ['A', 'B', 'C']
edges = [('A', 'B'), ('A', 'C')]

# Create a small graph from the node list and edge list
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Return the small graph
return G
