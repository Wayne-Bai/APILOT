
import networkx as nx

# Define the graph G
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('B', 'C')])

# Define a node n
n = 'A'

# Print short summary of information for the graph G or the node n
print(nx.info(G))
