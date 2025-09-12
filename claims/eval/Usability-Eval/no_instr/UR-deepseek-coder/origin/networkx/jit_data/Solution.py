import networkx as nx
import json

def to_jit_json(graph):
    nodes = [{"id": str(node)} for node in graph.nodes()]
    edges = [{"source": str(u), "target": str(v)} for u, v in graph.edges()]
    
    jit_data = {
        "nodes": nodes,
        "edges": edges
    }
    
    return json.dumps(jit_data, indent=2)

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
jit_json = to_jit_json(G)
print(jit_json)
