import networkx as nx
import json

# Create a new directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "A")
G.add_edge("A", "C")
G.add_edge("C", "B")

# JIT JSON format has two main sections: nodes and edges
def generate_jit_json(G):
    nodes = [{"id": n, "name": n} for n in G.nodes()]
    edges = [{"id": i, "source": e[0], "target": e[1]} for i, e in enumerate(G.edges())]
    return {"nodes": nodes, "edges": edges}

# Generate JIT JSON data
jit_json_data = generate_jit_json(G)

# Pretty print the JSON data
print(json.dumps(jit_json_data, indent=4))
