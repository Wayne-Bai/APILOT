import networkx as nx
import pickle

# Function to read graph object from Python pickle format
def read_graph_pickle(file_path):
    """
    Reads a graph object from a Python pickle file.

    Args:
    file_path (str): Path to the pickle file containing the graph object.

    Returns:
    G (networkx.Graph): The graph object read from the pickle file.
    """
    try:
        # Open the pickle file in binary mode
        with open(file_path, 'rb') as file:
            # Load the graph object from the pickle file
            G = pickle.load(file)
    except Exception as e:
        print(f"Error reading graph object from pickle file: {str(e)}")
        return None

    # Check if the loaded object is a NetworkX graph
    if isinstance(G, nx.Graph):
        return G
    else:
        print("Loaded object is not a NetworkX graph.")
        return None

# Example usage
file_path = 'graph.pkl'  # Replace with the path to your graph pickle file
G = read_graph_pickle(file_path)

# Print the graph's nodes and edges
if G is not None:
    print("Nodes:", list(G.nodes()))
    print("Edges:", list(G.edges()))
