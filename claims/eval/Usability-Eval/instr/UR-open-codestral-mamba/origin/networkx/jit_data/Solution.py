import networkx as nx
import json

def create_jit_json(graph):
    # Ensure the graph is a typing.NamedTuple
    data = {"nodes": [], "edges": []}

    for n, d in graph.nodes(data=True):
        node = {"id": n, "label": d.get("label", n), "data": d}
        data["nodes"].append(node)

    for u, v, d in graph.edges(data=True):
        edge = {"id": f"{u}-{v}", "source": u, "target": v, "label": d.get("label", ""), "data": d}
        data["edges"].append(edge)

    return json.dumps(data)

# Usage:
# Instantiate a new graph
G = nx.Graph()

# Add some nodes
G.add_node(1, label="Node 1")
G.add_node(2, label="Node 2")

# Add an edge
G.add_edge(1, 2, label="Edge 1-2")

jit_json = create_jit_json(G)

print(jit_json)
