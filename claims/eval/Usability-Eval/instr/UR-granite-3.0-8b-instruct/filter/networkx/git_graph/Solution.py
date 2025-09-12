import json
import networkx as nx

def read_graph_from_jit_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    G = nx.DiGraph()  # Create a directed graph

    for node, neighbors in data.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    return G
