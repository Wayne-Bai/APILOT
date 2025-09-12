import networkx as nx
import json

def graph_to_jit_json(graph):
    # Convert the graph to a dictionary representation
    graph_data = {
        "nodes": [],
        "edges": []
    }
    
    # Add nodes
    for node in graph.nodes(data=True):
        graph_data["nodes"].append({
            "id": node[0],
            **node[1]  # Include node attributes
        })
    
    # Add edges
    for edge in graph.edges(data=True):
        graph_data["edges"].append({
            "source": edge[0],
            "target": edge[1],
            **edge[2]  # Include edge attributes
        })
    
    # Convert to JSON format
    return json.dumps(graph_data)

# Example usage
G = nx.Graph()
G.add_node(1, label='A')
G.add_node(2, label='B')
G.add_edge(1, 2, weight=4)

jit_json_output = graph_to_jit_json(G)
print(jit_json_output)
