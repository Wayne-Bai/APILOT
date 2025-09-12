# Import necessary libraries
import networkx as nx
import pickle

# Load the graph object from the pickle file
def load_graph_from_pickle(pickle_file):
    """
    Load a graph object from a pickle file.
    
    Parameters:
    pickle_file (str): The path to the pickle file containing the graph object.
    
    Returns:
    nx.Graph: The loaded graph object.
    """
    try:
        with open(pickle_file, 'rb') as f:
            graph = pickle.load(f)
            return graph
    except Exception as e:
        print(f"Error loading graph from pickle file: {e}")
        return None

# Usage example:
pickle_file_path = 'path_to_your_pickle_file.pkl'  # Replace with your pickle file path
graph = load_graph_from_pickle(pickle_file_path)

# Check if the graph was loaded successfully
if graph is not None:
    print("Graph loaded successfully.")
    print(f"Graph type: {type(graph)}")
    print(f"Number of nodes: {graph.number_of_nodes()}")
    print(f"Number of edges: {graph.number_of_edges()}")
else:
    print("Failed to load graph from pickle file.")
