import yaml
import networkx as nx

# Function to read and write NetworkX graphs in YAML format
def read_and_write_graph(graph, filename):
    # Convert the NetworkX graph to data structures that can be serialized
    data = {"graph": nx.to_dict_of_dicts(graph)}

    # Write the data to the specified filename in YAML format
    with open(filename, 'w') as file:
        yaml.dump(data, file)

    return data

# Example usage:
G = nx.Graph() # Create a new graph
G.add_edges_from([(1, 2), (2, 3), (3, 1)]) # Add edges
write_contact_file = 'graph.yaml'
read_and_write_graph(G, write_contact_file)
# Load the graph back from the file
with open(write_contact_file) as file:
    graph_data = yaml.safe_load(file)

# Reconstruct the graph from the loaded data
loaded_graph = nx.node_link_graph(**graph_data['graph'])
print(networkx.info(loaded_graph))
