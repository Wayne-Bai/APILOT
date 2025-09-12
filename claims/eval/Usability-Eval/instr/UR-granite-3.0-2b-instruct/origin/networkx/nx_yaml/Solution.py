import networkx as nx
import yaml

# Function to write a NetworkX graph to a YAML file
def write_graph_to_yaml(graph, filename):
    with open(filename, 'w') as f:
        yaml.safe_dump(graph.to_dict(), f)

# Function to read a NetworkX graph from a YAML file
def read_graph_from_yaml(filename):
    with open(filename, 'r') as f:
        graph_dict = yaml.safe_load(f)
        return nx.Graph(graph_dict)

# Example usage:
# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)

# Write the graph to a YAML file
write_graph_to_yaml(G, 'graph.yaml')

# Read the graph from the YAML file
H = read_graph_from_yaml('graph.yaml')

# Print the nodes and edges of the read graph
print(H.nodes())
print(H.edges())
