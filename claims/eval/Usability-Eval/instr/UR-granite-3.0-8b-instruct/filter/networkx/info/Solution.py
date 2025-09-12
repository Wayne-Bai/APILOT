import networkx as nx

# Assuming G is your graph and n is a node in the graph
G = nx.Graph()  # or nx.DiGraph() for directed graph
G.add_node(n)

# Print short summary of information for the graph G
print(f"Graph G has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Print short summary of information for the node n
print(f"Node {n} has degree {G.degree(n)} and is connected to {list(G.neighbors(n))}.")
