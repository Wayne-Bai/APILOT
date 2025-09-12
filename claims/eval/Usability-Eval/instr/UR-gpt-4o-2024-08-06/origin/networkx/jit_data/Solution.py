import networkx as nx
import json

def graph_to_jit_json(G):
    # Create a structure to hold nodes and edges
    graph_struct = {
        "nodes": [],
        "edges": []
    }
    
    # Add nodes and their attributes
    for node in G.nodes(data=True):
        node_id = node[0]
        node_attrs = node[1]
        jit_node = {
            "id": node_id,
            "name": str(node_id),
            "data": node_attrs
        }
        graph_struct["nodes"].append(jit_node)
    
    # Add edges and their attributes
    for edge in G.edges(data=True):
        source = edge[0]
        target = edge[1]
        edge_attrs = edge[2]
        jit_edge = {
            "source": source,
            "target": target,
            "data": edge_attrs
        }
        graph_struct["edges"].append(jit_edge)
    
    # Convert the structure to JSON
    jit_json = json.dumps(graph_struct, indent=4)
    return jit_json

# Example usage:
# Create a sample graph
G = nx.Graph()
G.add_node(1, category='A')
G.add_node(2, category='B')
G.add_edge(1, 2, weight=4.2)

# Get JIT JSON representation
jit_json = graph_to_jit_json(G)
print(jit_json)
