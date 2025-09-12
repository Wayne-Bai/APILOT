import networkx as nx
import numpy as np

def convert_dict_to_1d_array(dictionary, mapping=None):
    # Create an empty graph
    G = nx.Graph()

    # Add edges to the graph based on the dictionary keys
    for key in dictionary.keys():
        G.add_edge(key, dictionary[key])

    # Get the connected components in the graph
    connected_components = list(nx.connected_components(G))

    # Map the connected components to a 1d numpy array
    if mapping:
        mapped_array = np.array([mapping[cc] for cc in connected_components])
    else:
        mapped_array = np.array(connected_components)

    return mapped_array

# Example usage
dictionary = {1: 2, 3: 4, 5: 6}
mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}

mapped_array = convert_dict_to_1d_array(dictionary, mapping)
print(mapped_array)
