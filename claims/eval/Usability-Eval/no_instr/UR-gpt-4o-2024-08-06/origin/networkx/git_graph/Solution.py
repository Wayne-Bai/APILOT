import networkx as nx
import json

def read_graph_from_jit_json(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    
    # Create an empty graph
    G = nx.Graph()

    # Assuming the json_data is structured in JIT JSON format
    # Nodes and edges need to be added based on their respective sections

    # Adding nodes
    for node_info in data['nodes']:
        node_id = node_info['id']
        # You can also add other node attributes here if needed
        G.add_node(node_id)

    # Adding edges
    for edge_info in data['edges']:
        source = edge_info['source']
        target = edge_info['target']
        # You can add edge attributes if present in the edge_info dictionary
        G.add_edge(source, target)

    return G

# Example JIT JSON data
jit_json_data = '''
{
    "nodes": [
        {"id": "1"},
        {"id": "2"},
        {"id": "3"}
    ],
    "edges": [
        {"source": "1", "target": "2"},
        {"source": "2", "target": "3"}
    ]
}
'''

# Read the graph from JIT JSON data
graph = read_graph_from_jit_json(jit_json_data)

# Print the nodes and edges
print("Nodes:", list(graph.nodes))
print("Edges:", list(graph.edges))
