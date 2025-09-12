import networkx as nx
import json

def create_graph():
    # Create a new empty graph
    G = nx.Graph()

    # Add nodes
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)

    # Add edges
    G.add_edge(1, 2, weight=3)
    G.add_edge(2, 3, weight=1)
    G.add_edge(3, 4, weight=2)
    G.add_edge(4, 1, weight=4)

    return G

def graph_to_jit_json(G):
    # Create a dictionary to hold the graph data
    graph_data = {}

    # Add the nodes
    graph_data['nodes'] = [{'id': node, 'name': str(node)} for node in G.nodes]

    # Add the edges
    graph_data['edges'] = [{'id': 'e' + str(edge[0]) + '-' + str(edge[1]), 
                           'source': edge[0], 
                            'target': edge[1], 
                            'weight': G.get_edge_data(*edge)['weight']} 
                           for edge in G.edges]

    return json.dumps(graph_data)

# Create a graph
G = create_graph()

# Convert the graph to JIT JSON format
jit_json = graph_to_jit_json(G)

# Print the JIT JSON
print(jit_json)
