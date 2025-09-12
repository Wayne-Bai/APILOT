import json
import networkx as nx

# Sample graph data
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "A"), ("A", "D")])

# Convert graph to JSON format
graph_data = {
    "nodes": list(G.nodes),
    "edges": [(u, v) for u, v in G.edges]
}

# Return data in JIT JSON format
json_data = json.dumps(graph_data)

print(json_data)
