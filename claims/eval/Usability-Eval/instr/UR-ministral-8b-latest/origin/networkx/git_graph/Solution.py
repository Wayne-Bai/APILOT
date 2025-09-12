import json
import networkx as nx

# Reading the graph from a JIT JSON format
with open('graph.jit.json', 'r') as file:
    graph_data = json.load(file)

# Create a directed graph from JSON
G = nx.DiGraph()
for node, neighbors in graph_data.items():
    G.add_node(node)
    G.add_edges_from([(node, neighbor) for neighbor in neighbors])

# To see the nodes and edges in the created graph
print("Nodes of graph: ")
print(G.nodes)

print("Edges of graph: ")
print(G.edges)

# You can further manipulate the graph as needed
