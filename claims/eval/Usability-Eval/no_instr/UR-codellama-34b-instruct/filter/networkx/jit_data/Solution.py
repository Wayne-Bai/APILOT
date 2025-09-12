import networkx as nx

# Create a DiGraph object
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(["A", "B", "C"])
G.add_edges_from([("A", "B"), ("B", "C")])

# Get the JIT JSON data for the graph
jit_data = nx.readwrite.json_graph.node_link_data(G)

# Print the JIT JSON data to the console
print(jit_data)
