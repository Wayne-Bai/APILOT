import networkx as nx
from IPython.display import display

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['Node1', 'Node2', 'Node3'])
G.add_edges_from([('Node1', 'Node2'), ('Node2', 'Node3')])

# Display the graph
display(G)
