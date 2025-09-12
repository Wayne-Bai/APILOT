import networkx as nx
import json

def graph_to_jit_json(graph):
    # Convert the NetworkX graph into a format suitable for JIT JSON
    data = {
        "nodes": [{"id": node} for node in graph.nodes()],
        "links": [{"source": u, "target": v} for u, v in graph.edges()]
    }
    return json.dumps(data)

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

jit_json = graph_to_jit_json(G)
print(jit_json)
