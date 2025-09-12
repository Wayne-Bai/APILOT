
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1, label='Node 1')
G.add_node(2, label='Node 2')
G.add_node(3, label='Node 3')

# Set a unique node label for each node in the graph
for node in G.nodes:
    if G.degree(node) > 1:
        G.nodes[node]['label'] = f"{G.nodes[node]['label']} ({G.nodes[node].index})"
