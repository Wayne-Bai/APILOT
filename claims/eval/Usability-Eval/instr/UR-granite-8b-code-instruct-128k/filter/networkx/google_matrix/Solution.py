
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(1, 3)

# Get the Google matrix of the graph
google_matrix = nx.to_numpy_matrix(G, nodelist=sorted(G))

# Print the Google matrix
print(google_matrix)
