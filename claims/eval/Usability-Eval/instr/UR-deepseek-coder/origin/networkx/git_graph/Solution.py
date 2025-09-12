import networkx as nx
import json

def read_graph_from_jit_json(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    
    # Create an empty graph
    G = nx.Graph()
    
    # Add nodes
    for node in data['nodes']:
        G.add_node(node['id'], **node['attributes'])
    
    # Add edges
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], **edge['attributes'])
    
    return G

# Example usage:
# json_data = '{"nodes": [{"id": 1, "attributes": {"label": "Node1"}}, {"id": 2, "attributes": {"label": "Node2"}}], "edges": [{"source": 1, "target": 2, "attributes": {"weight": 1}}]}'
# graph = read_graph_from_jit_json(json_data)
# print(graph.nodes(data=True))
# print(graph.edges(data=True))
