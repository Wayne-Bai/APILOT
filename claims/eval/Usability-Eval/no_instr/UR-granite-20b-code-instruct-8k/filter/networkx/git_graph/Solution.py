import networkx as nx

# read graph from JIT JSON
G = nx.readwrite.json_graph.jit_graph_from_file('graph.json')
