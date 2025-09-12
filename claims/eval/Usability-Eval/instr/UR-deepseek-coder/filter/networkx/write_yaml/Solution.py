import networkx as nx
import yaml

def graph_to_yaml(graph, path):
    # Create a dictionary to hold the graph data
    graph_data = {
        'nodes': list(graph.nodes(data=True)),
        'edges': list(graph.edges(data=True))
    }
    
    # Write the dictionary to a YAML file
    with open(path, 'w') as file:
        yaml.dump(graph_data, file, default_flow_style=False)

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 3)])
graph_to_yaml(G, 'graph.yaml')
