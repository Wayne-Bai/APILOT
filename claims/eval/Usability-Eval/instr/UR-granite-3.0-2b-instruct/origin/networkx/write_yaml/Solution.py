import networkx as nx
import yaml

# Create a graph G
G = nx.Graph()

# Add nodes to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Add edges to the graph
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "C")

# Write the graph to a YAML file
with open("G.yaml", "w") as file:
    yaml.dump(G.to_dict(), file)
