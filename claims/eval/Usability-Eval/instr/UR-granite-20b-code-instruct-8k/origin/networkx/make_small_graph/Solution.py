import networkx as nx

graph_description = {...}  # Define the graph description here

# Create a new graph object
G = nx.Graph()

# Add nodes and edges to the graph based on the graph_description
for node, edges in graph_description.items():
    G.add_node(node)
    for edge in edges:
        G.add_edge(node, edge)

# Print the graph
print(G.nodes(data=True))
print(G.edges(data=True))
