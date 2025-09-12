import networkx as nx
import json

def graph_to_jit_json(graph):
    jit_json = {
        "id": "graph",
        "name": "Graph",
        "data": {},
        "children": []
    }
    
    node_dict = {}
    for node in graph.nodes():
        node_dict[node] = {
            "id": str(node),
            "name": str(node),
            "data": {
                "attributes": graph.nodes[node]
            },
            "children": []
        }
    
    for edge in graph.edges(data=True):
        source = edge[0]
        target = edge[1]
        
        # Add only target as child to avoid duplicates
        connection = {
            "id": str(target),
            "name": str(target),
            "data": {
                "attributes": graph.nodes[target],
                "connection": edge[2]  # edge attributes
            },
            "children": []
        }
        node_dict[source]['children'].append(connection)
    
    jit_json["children"] = list(node_dict.values())
    
    return json.dumps(jit_json, indent=4)

# Example usage
G = nx.Graph()
G.add_node(1, attribute="value1")
G.add_node(2, attribute="value2")
G.add_edge(1, 2, weight=10)

jit_json_output = graph_to_jit_json(G)
print(jit_json_output)
