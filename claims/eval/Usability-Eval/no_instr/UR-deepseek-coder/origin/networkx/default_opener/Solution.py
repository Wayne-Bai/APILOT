import networkx as nx
import os

def open_file_with_default_program(filename):
    # Create a graph to represent the file and its default program
    G = nx.DiGraph()
    G.add_node(filename, type='file')
    G.add_node('default_program', type='program')
    G.add_edge(filename, 'default_program', action='open')

    # Use the system's default program to open the file
    os.startfile(filename)

# Example usage
filename = "example.txt"
open_file_with_default_program(filename)
