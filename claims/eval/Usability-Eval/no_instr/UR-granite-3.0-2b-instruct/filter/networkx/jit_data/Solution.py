import networkx as nx
import json

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Function to get nodes and edges data in JIT JSON format
def get_data_in_jit_json():
    nodes = list(G.nodes)
    edges = list(G.edges)

    # Convert nodes to dictionary with their degrees
    nodes_data = {node: G.degree(node) for node in nodes}

    # Convert edges to dictionary with their weights
    edges_data = {(u, v): G[u][v].get('weight', 1) for u, v in edges}

    # Combine nodes and edges data
    data = {
        "nodes": nodes_data,
        "edges": edges_data
    }

    # Convert data to JSON
    json_data = json.dumps(data)

    return json_data

# Print the data in JIT JSON format
print(get_data_in_jit_json())
