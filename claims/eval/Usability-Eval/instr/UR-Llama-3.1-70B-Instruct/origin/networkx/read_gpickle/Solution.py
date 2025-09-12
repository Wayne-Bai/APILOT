import networkx as nx
import pickle

def read_graph_from_pickle(file_path):
    """
    Reads a graph object from a Python pickle file.

    Parameters:
    file_path (str): The path to the pickle file.

    Returns:
    graph (nx.Graph): The graph object read from the pickle file.
    """
    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Load the graph object from the pickle file
            graph = pickle.load(file)
            return graph
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None

# Example usage
file_path = 'graph.pkl'  # Replace with your file path
graph = read_graph_from_pickle(file_path)

if graph is not None:
    print("Graph loaded successfully.")
    print("Number of nodes: ", graph.number_of_nodes())
    print("Number of edges: ", graph.number_of_edges())
else:
    print("Failed to load graph.")
