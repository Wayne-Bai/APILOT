# Import the networkx library
import networkx as nx

# Create a new directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')
G.add_edge('A', 'D')
G.add_edge('D', 'E')
G.add_edge('E', 'F')
G.add_edge('F', 'D')

# Add nodes with additional attributes
G.add_node('G', attr='node_attribute')
G.add_edge('A', 'G')

# Print the graph
print("Nodes:", G.nodes(data=True))
print("Edges:", G.edges(data=True))

# Pickle the graph
nx.write_gpickle(G, "graph.pkl")

# Load the pickled graph
loaded_G = nx.read_gpickle("graph.pkl")

# Print the loaded graph
print("\nLoaded Graph:")
print("Nodes:", loaded_G.nodes(data=True))
print("Edges:", loaded_G.edges(data=True))
