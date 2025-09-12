import networkx as nx

def generate_jit_json(data):
    """
    Generates JIT JSON data from the given input data.
    
    Parameters:
    data (dict): Input data in dictionary format
    
    Returns:
    str: JIT JSON data in string format
    """
    # Create a new graph object
    G = nx.Graph()
    
    # Add nodes to the graph
    for node, attributes in data['nodes'].items():
        G.add_node(node, **attributes)
    
    # Add edges to the graph
    for edge, attributes in data['edges'].items():
        u, v = edge
        G.add_edge(u, v, **attributes)
    
    # Convert the graph to JIT JSON format
    jit_json_data = nx.readwrite.json_graph.jit_data(G)
    
    return jit_json_data
