import networkx as nx
import json

# Load the JIT JSON data from a file
def load_jit_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Create a directed graph from JIT JSON data
def create_graph(data):
    G = nx.DiGraph()
    for node in data['nodes']:
        G.add_node(node['id'])
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'])
    return G

# Read a graph from JIT JSON file and print its nodes and edges
def read_jit_json_graph(filename):
    data = load_jit_json(filename)
    G = create_graph(data)
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())
    print("Graph Adjacency List:", dict(G.adjacency()))

# Usage example
read_jit_json_graph('graph.jit.json')
