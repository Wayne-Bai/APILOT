import networkx as nx

# Load the graph from the pickle file
with open("graph.pkl", "rb") as f:
    G = nx.read_gpickle(f)

# Print the nodes and edges of the graph
print("Nodes:", list(G.nodes()))
print("Edges:", list(G.edges()))
