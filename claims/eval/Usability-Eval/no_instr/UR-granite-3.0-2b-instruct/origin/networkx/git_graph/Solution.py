import networkx as nx

# Read a graph from JIT JSON
G = nx.read_json('graph.json')

# Print the graph
print(G.edges)
