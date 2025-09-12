import networkx as nx
import json

def read_jit_graph(json_file):
    """
    Read a graph from JIT JSON file.
    
    Parameters:
    json_file (str): The path to the JIT JSON file.
    
    Returns:
    G (networkx.MultiGraph): The graph object.
    """
    
    # Open the JIT JSON file in read mode
    with open(json_file, 'r') as file:
        # Load the JIT JSON data into a dictionary
        jit_data = json.load(file)
        
    # Initialize an empty graph
    G = nx.Graph()
    
    # Add nodes to the graph
    nodes = jit_data['nodes']
    for node in nodes:
        # Extract node attributes
        id = node['id']
        label = node['label']
        G.add_node(id, label=label)
        
        # Extract neighbors
        neighbors = node['neighbors']
        if isinstance(neighbors, list):  # In some JIT JSON files, 'neighbors' is an array
            for neighbor_id in neighbors:
                G.add_edge(id, neighbor_id)
        else:
            # In some JIT JSON files, 'neighbors' is an object (not an array)
            G.add_edges_from([(id, nei_id) for nei_id in neighbors.values()])
            
    # Add edge attributes
    edges = jit_data['edges']
    for edge in edges:
        # Extract edge attributes
        src = edge['source']
        dst = edge['target']
        weights = edge['weight']
        G[src][dst]['weight'] = weights
        
    return G

# Example usage
json_file = 'path_to_your_jit_json_file.json'
G = read_jit_graph(json_file)
print(G.nodes())
print(G.edges())
