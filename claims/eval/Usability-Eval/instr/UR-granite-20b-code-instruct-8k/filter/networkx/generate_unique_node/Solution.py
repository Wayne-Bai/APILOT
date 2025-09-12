
import networkx as nx
# Create a new graph object
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Generate unique node labels
node_labels = {node:str(idx) for idx, node in enumerate(G.nodes())}
nx.set_node_attributes(G, node_labels, 'label')
