import networkx as nx
import json

def graph_to_json(graph):
    node_data = {}
    for node in graph.nodes:
        node_data[node] = graph.nodes[node]

    edge_data = {}
    for edge in graph.edges:
        edge_data[edge] = graph.edges[edge]

    data = {
        "nodes": node_data,
        "edges": edge_data
    }

    return json.dumps(data)

# Example usage:
G = nx.Graph()
G.add_node(1, name="Node 1")
G.add_node(2, name="Node 2")
G.add_edge(1, 2, weight=0.5)

print(graph_to_json(G))
