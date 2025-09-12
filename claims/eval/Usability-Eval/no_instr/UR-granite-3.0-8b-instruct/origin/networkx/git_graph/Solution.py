import networkx as nx

# Read the graph from JIT JSON
def read_graph_from_jit_json(file_path):
    G = nx.read_jit(file_path)
    return G

# Usage
file_path = "path/to/your/graph.jit.json"
G = read_graph_from_jit_json(file_path)
