
import networkx as nx

# Define the graph
G = nx.DiGraph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 5)

# Print short summary of the graph
print("Short summary of the graph:")
print(nx.info(G))
