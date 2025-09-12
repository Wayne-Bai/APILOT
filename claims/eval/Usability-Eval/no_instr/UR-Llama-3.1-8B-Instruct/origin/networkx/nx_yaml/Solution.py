import networkx as nx
import yaml

# Create a new graph
G = nx.Graph()

# Add some nodes and edges to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("A", "C")

# Write the graph to a YAML file
with open("graph.yaml", "w") as f:
    nx.write_yaml(G, f)

# Read the graph from a YAML file
with open("graph.yaml", "r") as f:
    loaded_graph = nx.read_yaml(f)

print("Graph nodes:", loaded_graph.nodes())
print("Graph edges:", loaded_graph.edges())

# Alternatively, you can also use the following code to read the graph from a YAML file
with open("graph.yaml", "r") as f:
    graph_data = yaml.safe_load(f)
loaded_graph = nx.parse_yaml(graph_data)
print("Graph nodes:", loaded_graph.nodes())
print("Graph edges:", loaded_graph.edges())
