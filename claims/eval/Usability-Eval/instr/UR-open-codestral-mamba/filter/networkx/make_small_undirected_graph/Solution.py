import networkx as nx

# Undirected graph description
graph_description = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')]

# Create the graph
GRAPH = nx.Graph()

# Add edges to the graph based on the description
GRAPH.add_edges_from(graph_description)

# Display the number of nodes and edges in the graph
print("Number of nodes:", GRAPH.number_of_nodes())
print("Number of edges:", GRAPH.number_of_edges())
