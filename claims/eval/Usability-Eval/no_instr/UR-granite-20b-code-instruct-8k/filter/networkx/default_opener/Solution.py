import networkx as nx
import os

def open_file_with_default_program(filename):
    """
    Opens the file with the system's default program.
    
    Args:
        filename (str): The name of the file to open.
    """
    # Create a graph with a single node representing the file
    G = nx.Graph()
    G.add_node(filename)
    
    # Open the file with the system's default program
    os.startfile(filename)
