import networkx as nx
import json

def graph_to_jit_json(graph):
    jit_json = {
        'nodes': [],
        'edges': []
    }
    
    for node in graph.nodes(data=True):
        jit_node = {
            'id': str(node[0]),
            'name': node[1].get('name', str(node[0])),
            'data': {k: v for k, v in node[1].items() if k != 'name'}
        }
        jit_json['nodes'].append(jit_node)
        
    for source, target, attrs in graph.edges(data=True):
        jit_edge = {
            'nodeFrom': str(source),
            'nodeTo': str(target),
            'data': attrs
        }
        jit_json['edges'].append(jit_edge)
    
    return jit_json

# Example of creating a graph
G = nx.Graph()
G.add_node(1, name="Node 1", weight=5)
G.add_node(2, name="Node 2", weight=3)
G.add_edge(1, 2, weight=1.5)
G.add_edge(1, 1) # self loop

# Generate JIT JSON
jit_data = graph_to_jit_json(G)
jit_json_string = json.dumps(jit_data, indent=4)
print(jit_json_string)
