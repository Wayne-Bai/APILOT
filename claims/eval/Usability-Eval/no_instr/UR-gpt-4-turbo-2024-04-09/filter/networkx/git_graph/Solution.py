import networkx as nx
import json

# Function to read a graph from JIT JSON format
def read_jit_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    G = nx.Graph()

    for node in data:
        G.add_node(node['id'])
        for adj in node.get('adjacencies', []):
            G.add_edge(node['id'], adj['nodeTo'], weight=adj.get('data', {}).get('weight', 1))

    return G

# Example usage:
jit_json_file = 'path_to_your_jit_json.json'  # Specify the path to your JIT JSON file
graph = read_jit_json(jit_json_file)
print(nx.info(graph))
