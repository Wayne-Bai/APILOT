import networkx as nx

# Create a sample graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Print a short summary of the graph
summary = nx.info(G)
print(summary)

# If you want a short summary for a specific node
node = 1
if node in G:
    node_summary = f"Node {node}: {G.degree[node]} edge(s)"
    print(node_summary)
else:
    print(f"Node {node} not in graph")
