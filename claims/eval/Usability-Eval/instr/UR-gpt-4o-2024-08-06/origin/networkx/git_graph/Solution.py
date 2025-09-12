import networkx as nx
import json

def read_graph_from_jit_json(jit_json_string):
    # Parse the JSON string into a Python dictionary
    data = json.loads(jit_json_string)
    
    # Create an empty directed graph
    G = nx.DiGraph() if data.get('directed', False) else nx.Graph()
    
    # Add nodes and their attributes
    for node in data['nodes']:
        G.add_node(node['id'], **node.get('data', {}))
    
    # Add edges and their attributes
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], **edge.get('data', {}))
    
    return G

# Example JIT JSON representation
jit_json = '''
{
    "nodes": [
        {"id": "1", "data": {"label": "Node 1"}},
        {"id": "2", "data": {"label": "Node 2"}}
    ],
    "edges": [
        {"source": "1", "target": "2", "data": {"weight": 1}}
    ],
    "directed": true
}
'''

# Read the graph from the JIT JSON
graph = read_graph_from_jit_json(jit_json)

# Printing nodes and edges
print("Nodes:")
print(graph.nodes(data=True))
print("Edges:")
print(graph.edges(data=True))
