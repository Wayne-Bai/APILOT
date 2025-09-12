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
# json_data = '{"nodes": [{"id": 1, "attributes": {"color": "red"}}, {"id": 2, "attributes": {"color": "blue"}}], "edges": [{"source": 1, "target": 2, "attributes": {"weight": 10}}]}'
# graph = read_graph_from_jit_json(json_data)
# print(graph.nodes(data=True))
# print(graph.edges(data=True))
