import networkx as nx
import json

def read_graph_from_json(file_path):
    """
    Read a graph from a JIT JSON file.
    
    Parameters:
    file_path (str): The path to the JSON file.
    
    Returns:
    G (nx.Graph): The graph object.
    """
    # Load the JSON data from the file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Create an empty directed graph
    G = nx.DiGraph()
    
    # Populate the graph using the JSON data
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'])
    
    return G

# Usage
file_path = 'graph.json'  # Replace with your JSON file path
G = read_graph_from_json(file_path)
print(G.nodes())  # Print the nodes of the graph
print(G.edges())  # Print the edges of the graph
