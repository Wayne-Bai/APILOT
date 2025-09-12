import networkx as nx
import yaml

def save_graph_to_yaml(G, filename):
    edges = [(u, v, data) for u, v, data in G.edges(data=True)]

    graph_data = {
        "nodes": list(G.nodes()),
        "edges": edges
    }

    with open(filename, 'w') as file:
        yaml.dump(graph_data, file)

# Example usage:
# Create a graph
G = nx.Graph()
G.add_node('A')
G.add_node('B')
G.add_edge('A', 'B', weight=1.0)

# Save the graph to a YAML file
save_graph_to_yaml(G, 'graph.yaml')
