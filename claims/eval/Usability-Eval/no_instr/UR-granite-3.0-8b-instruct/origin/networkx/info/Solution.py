import networkx as nx

# Assuming G is your graph and n is a node in the graph
G = nx.Graph()  # Create a new graph
G.add_node(n)  # Add a node to the graph
G.add_edge(n, n)  # Add an edge to the graph

# Print short summary of information for the graph G
print("Graph G has", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges.")

# Print short summary of information for the node n
print("Node", n, "has", G.degree(n), "edges.")
