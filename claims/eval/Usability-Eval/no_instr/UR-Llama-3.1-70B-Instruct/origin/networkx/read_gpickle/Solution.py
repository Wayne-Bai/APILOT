# Import necessary libraries
import networkx as nx
import pickle

# Function to read graph object from Python pickle format
def read_graph_from_pickle(file_path):
    """
    Reads a graph object from Python pickle format.

    Args:
        file_path (str): Path to the pickle file.

    Returns:
        nx.Graph: The read graph object.
    """
    try:
        with open(file_path, 'rb') as f:
            graph = pickle.load(f)
            if not isinstance(graph, nx.Graph):
                raise ValueError("The unpickled object is not a networkx Graph.")
            return graph
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except pickle.UnpicklingError:
        print(f"Failed to unpickle the file {file_path}.")
        return None

# Example usage:
if __name__ == "__main__":
    file_path = "graph.pickle"  # replace with your file path
    graph = read_graph_from_pickle(file_path)

    if graph is not None:
        print("Graph info:")
        print(nx.info(graph))
