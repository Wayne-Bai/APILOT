import networkx as nx
import yaml

def graph_to_yaml(G, path):
    # Convert the graph to a dictionary
    graph_data = {
        'nodes': [{'id': node} for node in G.nodes()],
        'edges': [{'source': u, 'target': v} for u, v in G.edges()]
    }
    
    # Write the dictionary to a YAML file
    with open(path, 'w') as file:
        yaml.dump(graph_data, file, default_flow_style=False)

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
graph_to_yaml(G, 'graph.yaml')
