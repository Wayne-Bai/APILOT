
import yaml
from networkx import Graph

# Create a graph
G = Graph()

# Add nodes and edges to the graph
G.add_node("A")
G.add_node("B")
G.add_edge("A", "B")

# Write the graph to a file in YAML format
with open("graph.yaml", "w") as f:
    yaml.dump(G, f)
