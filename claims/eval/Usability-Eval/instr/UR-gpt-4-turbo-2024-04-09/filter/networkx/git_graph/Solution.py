import networkx as nx
import json

def read_graph_from_jit_json(json_file):
    # Load JSON data from a file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Create a new graph
    G = nx.Graph()

    # Assuming the JSON structure has nodes list and edges list as often used in JIT JSON formats
    for node in data['nodes']:
        G.add_node(node['id'], **node['data'])

    for edge in data['edges']:
        G.add_edge(edge['nodeFrom'], edge['nodeTo'], **edge['data'])

    return G

# Example usage to read a graph
# G = read_graph_from_jit_json('path_to_your_json_file.json')
# print(G.nodes(data=True))
# print(G.edges(data=True))
