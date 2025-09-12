import networkx as nx
import pickle

def create_and_write_graph(filename, directed=False):
    """
    Create a graph and write it in Python pickle format.
    
    Parameters:
    filename (str): The filename where the graph will be saved.
    directed (bool): If True, the graph will be directed, otherwise undirected. Default is False.
    """
    
    # Create a new graph
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Add some nodes and edges to the graph
    G.add_node("A")
    G.add_node("B")
    G.add_node("C")
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("C", "A")
    
    # Write the graph in Python pickle format
    with open(filename, 'wb') as file:
        pickle.dump(G, file)

# Call the function to create and write a graph
create_and_write_graph('graph.pickle')

# To read the graph from the file, you can use the following code:
def read_graph(filename):
    """
    Read a graph from a file in Python pickle format.
    
    Parameters:
    filename (str): The filename where the graph is saved.
    
    Returns:
    nx.Graph: The graph read from the file.
    """
    with open(filename, 'rb') as file:
        G = pickle.load(file)
    return G

G = read_graph('graph.pickle')
print(G.nodes())
print(G.edges())
