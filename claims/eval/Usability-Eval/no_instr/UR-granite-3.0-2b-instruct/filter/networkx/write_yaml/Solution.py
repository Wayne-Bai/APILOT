import networkx as nx
import yaml

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node("A")
G.add_node("B")
G.add_edge("A", "B")

# Save the graph to a YAML file
with open("G.yaml", "w") as file:
    yaml.dump(G.to_dict_of_lists(), file)
