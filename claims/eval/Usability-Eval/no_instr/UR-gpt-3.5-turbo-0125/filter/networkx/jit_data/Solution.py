
import networkx as nx

def generate_jit_json(graph):
    jit_json = {"name": "flare", "children": []}
    
    for node in graph.nodes():
        node_data = {"name": node, "children": []}
        
        for successor in graph.successors(node):
            successor_data = {"name": successor}
            node_data["children"].append(successor_data)
        
        jit_json["children"].append(node_data)
    
    return jit_json

# Example usage
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (1, 3), (2, 3)])

jit_json_data = generate_jit_json(G)
print(jit_json_data)
